"""Code descriptions (based on
   http://www.consultant.ru/document/cons_doc_LAW_103394/c8c663513ad32e5a0eb8ca96753ea3e0911415db/)
"""

ACCOUNT_NAMES_TEXT = """БУХГАЛТЕРСКИЙ БАЛАНС	1000
Итого внеоборотных активов	1100
Нематериальные активы	1110
Результаты исследований и разработок	1120
Нематериальные поисковые активы	1130
Материальные поисковые активы	1140
Основные средства	1150
Доходные вложения в материальные ценности	1160
Финансовые вложения	1170
Отложенные налоговые активы	1180
Прочие внеоборотные активы	1190
Итого оборотных активов	1200
Запасы	1210
Налог на добавленную стоимость по приобретенным ценностям	1220
Дебиторская задолженность	1230
Финансовые вложения (за исключением денежных эквивалентов)	1240
Денежные средства и денежные эквиваленты	1250
Прочие оборотные активы	1260
БАЛАНС (актив)	1600
Итого капитал	1300
Уставный капитал (складочный капитал, уставный фонд, вклады товарищей)	1310
Собственные акции, выкупленные у акционеров	1320
Переоценка внеоборотных активов	1340
Добавочный капитал (без переоценки)	1350
Резервный капитал	1360
Нераспределенная прибыль (непокрытый убыток)	1370
Долгосрочные заемные средства	1410
Отложенные налоговые обязательства	1420
Оценочные обязательства	1430
Прочие долгосрочные обязательства	1450
Итого долгосрочных обязательств	1400
Краткосрочные заемные обязательства	1510
Краткосрочная кредиторская задолженность	1520
Доходы будущих периодов	1530
Оценочные обязательства	1540
Прочие краткосрочные обязательства	1550
Итого краткосрочных обязательств	1500
БАЛАНС (пассив)	1700
ОТЧЕТ О ФИНАНСОВЫХ РЕЗУЛЬТАТАХ	2000
Выручка	2110
Себестоимость продаж	2120
Валовая прибыль (убыток)	2100
Коммерческие расходы	2210
Управленческие расходы	2220
Прибыль (убыток) от продаж	2200
Доходы от участия в других организациях	2310
Проценты к получению	2320
Проценты к уплате	2330
Прочие доходы	2340
Прочие расходы	2350
Прибыль (убыток) до налогообложения	2300
Текущий налог на прибыль	2410
Постоянные налоговые обязательства (активы)	2421
Изменение отложенных налоговых обязательств	2430
Изменение отложенных налоговых активов	2450
Прочее	2460
Чистая прибыль (убыток)	2400
Результат от переоценки внеоборотных активов, не включаемый в чистую прибыль (убыток)	2510
Результат от прочих операций, не включаемый в чистую прибыль (убыток) периода	2520
Совокупный финансовый результат периода	2500
Базовая прибыль (убыток) на акцию	2900
Разводненная прибыль (убыток) на акцию	2910
ОТЧЕТ О ДВИЖЕНИИ ДЕНЕЖНЫХ СРЕДСТВ	4000
Поступления - всего	4110
От продажи продукции, товаров, работ и услуг	4111
Арендных платежей, лицензионных платежей, роялти, комиссионных и иных аналогичных платежей	4112
От перепродажи финансовых вложений	4113
Прочие поступления	4119
Платежи - всего	4120
Поставщикам (подрядчикам) за сырье, материалы, работы, услуги	4121
В связи с оплатой труда работников	4122
Проценты по долговым обязательствам	4123
Налога на прибыль организаций	4124
Прочие платежи	4129
Сальдо денежных потоков от текущих операций	4100
Поступления - всего	4210
От продажи внеоборотных активов (кроме финансовых вложений)	4211
От продажи акций других организаций (долей участия)	4212
От возврата предоставленных займов, от продажи долговых ценных бумаг (прав требования денежных средств к другим лицам)	4213
Дивидендов, процентов по долговым финансовым вложениям и аналогичных поступлений от долевого участия в других организациях	4214
Прочие поступления	4219
Платежи - всего	4220
В связи с приобретением, созданием, модернизацией, реконструкцией и подготовкой к использованию внеоборотны активов	4221
В связи с приобретением акций других организаций (долей участия)	4222
В связи с приобретением долговых ценных бумаг (прав требования денежных средств к другим лицам), предоставление займов другим лицам	4223
Процентов по долговым обязательствам, включаемым в стоимость инвестиционного актива	4224
Прочие платежи	4229
Сальдо денежных потоков от инвестиционных операций	4200
Поступления - всего	4310
Получение кредитов и займов	4311
Денежных вкладов собственников (участников)	4312
От выпуска акций, увеличения долей участия	4313
От выпуска облигаций, векселей и других долговых ценных бумаг и др.	4314
Прочие поступления	4319
Платежи - всего	4320
Собственникам (участникам) в связи с выкупом у них акций (долей участия) организации или их выходом из состава участников	4321
На уплату дивидендов и иных платежей по распределению прибыли в пользу собственников (участников)	4322
В связи с погашением (выкупом) векселей и других долговы ценных бумаг, возврат кредитов и займов	4323
Прочие платежи	4329
Сальдо денежных потоков от финансовых операций	4300
Сальдо денежных потоков за отчетный период	4400
Остаток денежных средств и денежных эквивалентов на начало отчетного периода	4450
Остаток денежных средств и денежных эквивалентов на конец отчетного периода	4500
Величина влияния изменений курса иностранной валюты по отношению к рублю	4490
Остаток средств на начало отчетного года	6100
Поступило средств - всего	6200
Вступительные взносы	6210
Членские взносы	6215
Целевые взносы	6220
Добровольные имущественные взносы и пожертвования	6230
Прибыль от предпринимательской деятельности организации	6240
Прочие	6250
Использовано средств - всего	6300
Расходы на целевые мероприятия	6310
социальная и благотворительная помощь	6311
проведение конференций, совещаний, семинаров и т.п.	6312
иные мероприятия	6313
Расходы на содержание аппарата управления	6320
расходы, связанные с оплатой труда (включая начисления)	6321
выплаты, связанные с оплатой труда	6322
расходы на служебные командировки и деловые поездки	6323
содержание помещений, зданий, автомобильного транспорта и иного имущества (кроме ремонта)	6324
ремонт основных средств и иного имущества	6325
прочие	6326
Приобретение основных средств, инвентаря и иного имущества	6330
Прочие	6350
Остаток средств на конец отчетного года	6400"""


def items_from_doc(doc: str):
    for x in doc.split("\n"):
        y = x.split("\t")
        try:
            yield y[1], y[0]
        except IndexError:
            raise ValueError(y)


def code_to_description(code: str, doc=ACCOUNT_NAMES_TEXT):
    """Return account text description by code."""
    acc_names = dict(items_from_doc(doc))
    return acc_names.get(code)


def okv(text):
    return f"Код ОКВЭД {text} уровня"


ADDITIONAL_DICT = {
    "ok1": okv("первого"),
    "ok2": okv("второго"),
    "ok3": okv("третьего"),
    "org": "Тип юридического лица (часть наименования организации)",
    "title": "Короткое название организации",
    "region": "Код региона по ИНН",
    "okpo": "Общероссийский классификатор предприятий и организаций (ОКПО)",
    "okopf": "Общероссийский классификатор организационно-правовых форм (ОКОПФ)",
    "okfs": "Общероссийский классификатор форм собственности (ОКФС)",
    "okved": "Общероссийский классификатор видов экономической деятельности (ОКВЭД)",
    "unit": "Код единицы измерения (384 - тыс. руб.)",
    "p": "Прибыль (убыток) до налогообложения",
}


def unlag(x):
    return x.replace("_lag", "") if x.endswith("_lag") else x


def whatis(varname: str, additional_codes: dict = ADDITIONAL_DICT):
    """Return text description for *varname*."""
    from boo.columns import MAPPER

    reverse = {v: k for k, v in MAPPER.items()}
    varname = unlag(varname)
    try:
        return additional_codes[varname]
    except KeyError:
        return code_to_description(reverse.get(varname))
