import argparse
import logging
import re
import datetime
import csv
logging.basicConfig(level=logging.INFO)


from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError
import news_page_objects as news
from common import config

logger = logging.getLogger(__name__)
is_well_formed_link = re.compile(r'^http?//.+/.+$')
is_root_path = re.compile(r'^/.+$')

def _new_scraper (new_site_uid):
    host = config()['news_sites'][new_site_uid]['url']
    logging.info('esta escaneando {}'.format(host))
    homepage = news.HomePage(new_site_uid,host)
    articles = []
    for link in homepage.article_links:
        article = _fetch_article(new_site_uid,host,link)
        if article:
            logger.info('encontro el ariculo')
            articles.append(article)
    _save_articles(new_site_uid,articles)

def _save_articles(new_site_uid,articles):
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    out_file_name = '{}_{}_resultado.csv'.format(new_site_uid,now)
    csv_headers = list(filter(lambda property: not property.startswith('_'), dir(articles[0])))

    with open(out_file_name, mode='w+',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)

        for article in articles:
            row = [str(getattr(article,prop))for prop in csv_headers]
            writer.writerow(row)


def _fetch_article(new_site_uid, host, link):
    logger.info('iniciando busqueda del articulo'+ link)
    article = None
    try:
        article = news.ArticlePage(new_site_uid,_build_link(host,link))
    except (HTTPError,MaxRetryError) as e:
        logger.warning('Error encontrando el error',exc_info=False)
    if article and not article.body:
        logger.warning('articulo invalido no tiene cuerpo')
        return None
    return article
        
def _build_link(host,link):
    if is_well_formed_link.match(link):
        return link
    elif is_root_path.match(link):
        return '{}{}'.format(host,link)
    else:
        return '{}/{}'.format(host,link)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    new_site_choices = list(config()['news_sites'].keys())
    parser.add_argument('new_site',help='el nuevo sitio al cual vas a scriptear', type=str,choices=new_site_choices)
    arg = parser.parse_args()
    _new_scraper(arg.new_site)