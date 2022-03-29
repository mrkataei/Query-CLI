from . import engine, MetaData, Integer, String, Column, Table


def create_adult_table():
    meta = MetaData()
    Table(
        'adults', meta,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('age', Integer, default=20),
        Column('workclass', String(15), default='Private'),
        Column('fnlwgt', String(10), default=None),
        Column('education', String(10), default='Bachelors'),
        Column('education-num', Integer, default=10),
        Column('marital-status', String(20), default='Never-married'),
        Column('occupation', String(20), default=None),
        Column('relationship', String(20), default=None),
        Column('race', String(12), default='white'),
        Column('sex', String(10), default='Male'),
        Column('capital-gain', Integer, default=0),
        Column('capital-loss', Integer, default=0),
        Column('hours-per-week', Integer, default=0),
        Column('native-country', String(20), default='United-States'),
        Column('native-country-trans', String(20), default='ایالت متحده آمریکا'),
        Column('salary', String(5), default='>50k')
    )
    try:
        meta.create_all(engine())
        return False
    except Exception as e:
        print(e)
        return True


def get_native_country(country: str):
    return engine().execute(f'SELECT COUNT(` sex`), ` sex` FROM `adults` '
                            f'WHERE ` native-country`= " {country}" GROUP BY ` sex`')


def add_adult(agel: int = 0, workclass: str = None, fnlwgt: str = None, education: str = None, edu_num: int = 0,
              mar_status: str = None, occupation: str = None,
              relationship: str = None, race: str = None, sex: str = None, cap_gain: int = 0, cap_loss: int = 0,
              h_p_week: int = 0, native_country: str = None,
              native_country_tr: str = None, salary: str = None):
    # try:
    engine().execute(f'insert into adults(age, ` workclass`, ` fnlwgt`, ` education`, ` education-num`,'
                     f' ` marital-status`, ` occupation`, ` relationship`, ` race`, ` sex`, ` capital-gain`,'
                     f' ` capital-loss`, ` hours-per-week`, ` native-country`, `native-country-trans`,'
                     f' ` salary`) '
                     f'VALUES ({agel},"{workclass}", "{fnlwgt}", "{education}", {edu_num},"{mar_status}",'
                     f' "{occupation}", "{relationship}", "{race}", "{sex}", {cap_gain}, {cap_loss}, {h_p_week},'
                     f' "{native_country}", "{native_country_tr}", "{salary}")')

# except Exception as e:
#     print(e)
