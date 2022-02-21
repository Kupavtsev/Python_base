# ORIGIN PROJECT
# mail-server / app.py

# In the first Part I we get [[{},{},{},{}]]

TWONY_TWO_DAYS = timedelta(22)

cur.execute("DELETE FROM public.anti WHERE ctid NOT IN (SELECT max(ctid) FROM public.anti GROUP BY public.anti.*);")
    cur.execute(
        f"""
        SELECT send_date, email, subscription, recipient from public.anti WHERE subscription > 0 AND recipient='{user}';
        """
        )
    result = cur.fetchall()

    result_list_total_data : list = []
    result_list : list = []
    result_list_periods : list = []
    for row in result:
        dict_key = {}
        dict_key["Send Date"] = row['send_date']
        dict_key["sender"] = row["email"]
        dict_key["Subscription"] = row["subscription"]
        dict_key["Recipient"] = row['recipient']
        result_list.append(dict_key)

# Second Part II
# In this part we do check period in 22 days between same sender
# on the last mail and previus 
# and create [{}]

    #   =============================================
    #   ====== Объеденяем даты по получателям =======
    #   =============================================
    # Словарь с отправителями из БД
    senders_periods_dict : dict = {}
   
    # Каждый словарь массива отправителей
    # 1
    for each_sender in range(len(result_list)):
        # print(result_list[each_sender])
        senders_periods_dict[result_list[each_sender]['sender']] = [[]]

    # Если ключ в senders_periods_dict равен значению sender в dict_key,
    # то поместить значение даты в массив значений senders_periods_dict
    for key, dates in sorted(senders_periods_dict.items()):
        for each_dict in range(len(result_list)):
            for each_sender in dates:
                if key == result_list[each_dict]['sender']:
                    each_sender.append(result_list[each_dict]['Send Date'])

     
    print('===================')
    # Проверка на периодичность
    quantity_of_periods = 0
    for k,v in senders_periods_dict.items():
        # print('\n')
        # print(k, ' : ')
        # print(type(v[0]))
        list_of_dates = v[0]
        
        # print(len(v[0]))
        if len((v[0])) > 1:
            # print(list_of_dates[0])
            # print(list_of_dates[1])
        #     print(senders_periods_dict['taco@trello.com'][0][v])
            print('pass')
            if list_of_dates[0] - list_of_dates[1] > TWONY_TWO_DAYS:
                periods_dict_key = {}
                periods_dict_key['Sender of Subscription'] = k
                periods_dict_key['Last Send Date'] = list_of_dates[0]
                periods_dict_key['Periods'] = len(list_of_dates)
                print('\n')
                print(k, ' : ')
                print(v)
                print('Subscription')
                quantity_of_periods += 1
                result_list_periods.append(periods_dict_key)
            else:
                pass

    #   ========================================
    #   ====== Даты по получателям конец =======
    #   ========================================

    result_list_total_data.append(result_list)
    result_list_total_data.append(result_list_periods)

# the result is [[{},{},{}][{},{},{}]]