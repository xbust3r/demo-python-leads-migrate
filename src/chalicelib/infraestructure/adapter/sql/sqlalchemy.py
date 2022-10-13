from abc import ABC
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, scoped_session

import os


class SqlAlchemyAdapter(ABC):
    session = None
    entity = None

    def __init__(self):
        self._session_maker()

    def create(self, entity):
        try:
            self.session.begin()
            self.session.add(entity)
            self.session.commit()
            return entity
        except Exception as e:
            self.session.rollback()
            raise e

    def update(self, entity):
        try:
            self.session.begin()
            self.session.commit()
            return entity
        except Exception as e:
            self.session.rollback()
            raise e

    def delete(self, id):
        try:
            result = self.find_by_id(id)
            self.session.delete(result)
            return self.session.commit()
        except Exception as e:
            raise e

    def find_all(self):
        try:
            result = self.session.query(self.entity)
            return result.all()
        except Exception as e:
            raise e

    def find_by_id(self, id):
        try:
            return self.session.query(self.entity).get(id)
        except Exception as e:
            raise e

    def find_by_slug(self, slug):
        try:
            return self.session.query(self.entity).get(slug)
        except Exception as e:
            raise e

    def _session_maker(self):
        # driver = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (self._options['username'],
        #                                                          self._options['password'],
        #                                                          self._options['host'],
        #                                                          self._options['port'],
        #                                                          self._options['database'])
        # host=os.environ['DB_HOST'], user=os.environ['DB_USER'], password=os.environ['DB_PASS'], db=os.environ['DB_NAME']
        driver = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (os.environ['DB_USER'],
                                                                  os.environ['DB_PASS'],
                                                                  os.environ['DB_HOST'],
                                                                  3306,
                                                                  os.environ['DB_NAME'])
        engine = create_engine(driver, echo=False, isolation_level='READ UNCOMMITTED', pool_recycle=180,
                               encoding='utf8')
        self.session = scoped_session(sessionmaker(bind=engine, autocommit=True))
