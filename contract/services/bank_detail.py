BANKS = {
    "307770": "AT А-Банк",
    "380946": "Авангард",
    "380548": "Агропросперис Банк",
    "322302": "IBOX bank",
    "380634": "АккордБанк",
    "380894": "Альпари",
    "320940": "Альтбанк",
    "300346": "Альфа-Банк",
    "300119": "Альянс",
    "322335": "Аркада",
    "353489": "Асвіо Банк",
    "34380645": "Банк 3/4",
    "380281": "Банк інвестицій і заощаджень",
    "321723": "БТА Банк",
    "307123": "Схід",
    "380526": "Глобус",
    "351607": "Грант",
    "380731": "Дойче Банк ДБУ",
    "377090": "Європейский Промисловий Банк",
    "305880": "Земельний Капітал",
    "336310": "Ідея Банк",
    "300539": "ІНГ Банк Украина",
    "313849": "Індустриалбанк",
    "300647": "Банк “Клірінговий Дом”",
    "312248": "Комінвестбанк",
    "322540": "Комерційний Індустріальний Банк",
    "307350": "Конкорд",
    "300614": "Креді Агріколь Банк",
    "305749": "Кредит Дніпро",
    "380366": "Кредит Європа Банк",
    "380441": "Кредитвест Банк",
    "325365": "Кредобанк",
    "339050": "Крісталбанк",
    "325268": "Львів",
    "351629": "Мегабанк",
    "380582": "Міжнародний Інвестиційний Банк",
    "313582": "Метабанк",
    "328760": "Місто Банк",
    "322001": "Універсал Банк",
    "313009": "Мотор-Банк",
    "325990": "Оксі Банк",
    "300528": "ОТП Банк",
    "300465": "Ощадбанк",
    "300506": "Перший Інвестиційний Банк",
    "328209": "Південний",
    "300658": "Піреус Банк МКБ",
    "353100": "Полікомбанк",
    "331489": "Полтава-банк",
    "339016": "Портал",
    "380838": "Правекс-Банк",
    "305299": "ПриватБанк",
    "320984": "ПроКредит Банк",
    "300012": "Промінвестбанк",
    "334851": "ПУМБ",
    "306500": "Радабанк",
    "300335": "Райффайзен Банк Аваль",
    "344443": "Розрахунковий центр",
    "339072": "РВС Банк",
    "320627": "Сбербанк",
    "380797": "СЕБ Корпоративний Банк",
    "300584": "Сітібанк",
    "380816": "Січ",
    "351254": "SkyBank",
    "339500": "ТАСкомбанк",
    "380106": "Траст-капитал",
    "380883": "Український Банк Реконструкції та Розвитку",
    "320371": "Український капітал",
    "320478": "Укргазбанк",
    "351005": "УкрСиббанк",
    "380377": "Укрбудінвестбанк",
    "322313": "УкрЕксімБанк",
    "334840": "Фамільний",
    "380418": "Форвард",
    "322539": "Юнекс Банк",
}


def get_mfo_code(iban: str) -> str:
    mfo = iban[4:10]
    if mfo in list(BANKS):
        return mfo
    else:
        return f""


def get_bank_name(mfo: str) -> str:
    return BANKS.get(mfo, "")