from . import adult, os, pd, engine, country, sql, add


def commands():
    while True:
        Subcommand = input('>').split(' ')
        if Subcommand[0] == "exit":
            os.system('exit()')
            break
        elif Subcommand[0] == "?":
            helpToString()
        else:
            runOSCommands(Subcommand)


def helpToString():
    print("insert <path.csv> (insert your csv in adult table database)\n"
          "add (add row in adult table) \n"
          "show <native-country> (the number of people per Sex of the given native-country.) \n")


def successToString():
    print("[OK] execution command success")


def runOSCommands(commands_arr):
    if commands_arr[0] == "show":
        if len(commands_arr) < 2:
            result = country(input('>Enter country plz:'))
        else:
            result = country(commands_arr[1])
        for res in result:
            print(res)
        successToString()
    elif commands_arr[0] == "add":
        try:
            age = int(input('>Enter age plz:(24)'))
        except ValueError:
            age = 24
        workclass = input('>Enter workclass plz:(Private)')
        workclass = 'Private' if not workclass else workclass

        fnlwgt = input('>Enter fnlwgt plz:(201490)')
        fnlwgt = '201490' if not fnlwgt else fnlwgt

        education = input('>Enter education plz:(Masters)')
        education = 'Masters' if not education else education

        try:
            edu_num = int(input('>Enter education-num plz:(10)'))
        except ValueError:
            edu_num = 10

        mar_status = input('>Enter mar_status plz:(Divorced)')
        mar_status = 'Divorced' if not mar_status else mar_status

        occupation = input('>Enter occupation plz:(Tech-support)')
        occupation = 'Tech-support' if not occupation else occupation

        relationship = input('>Enter relationship plz:(Husband)')
        relationship = 'Husband' if not relationship else relationship

        race = input('>Enter race plz:(White)')
        race = 'White' if not race else race

        sex = 'Male' if input('>Are you a man(y/n)?(default y)') == 'y' else 'Female'
        try:
            cap_gain = int(input('>Enter cap_gain plz:(0)'))
        except ValueError:
            cap_gain = 0
        try:
            cap_loss = int(input('>Enter cap_loss plz:(0)'))
        except ValueError:
            cap_loss = 0
        try:
            h_p_week = int(input('>Enter hours-per-week	plz:(0)'))
        except ValueError:
            h_p_week = 0

        native_country = input('>Enter native-country plz:(Iran)')
        native_country = 'Iran' if not native_country else native_country

        native_trans = input('>Enter native-country-trans plz:(ایران)')
        native_trans = 'ایران' if not native_trans else native_trans

        salary = '>50k' if input('>is your greater than 50k (y/n):(default y)') == 'y' else '<=50k'

        add(agel=age, workclass=workclass, fnlwgt=fnlwgt, education=education, edu_num=edu_num, mar_status=mar_status,
            occupation=occupation, relationship=relationship, race=race, sex=sex, cap_gain=cap_gain, cap_loss=cap_loss,
            h_p_week=h_p_week, native_country=native_country, native_country_tr=native_trans, salary=salary)
        successToString()
    elif commands_arr[0] == "insert":
        if os.path.exists(commands_arr[2]):
            with open(commands_arr[2], 'r') as file:
                data_df = pd.read_csv(file)
                eng = engine()
                data_df.to_sql('adults', con=eng, index=False, if_exists='replace',
                               dtype={'age': sql.types.Integer,
                                      ' workclass': sql.types.String(15),
                                      ' fnlwgt': sql.types.String(15),
                                      ' education': sql.types.String(10),
                                      ' education-num': sql.Integer,
                                      ' marital-status': sql.types.String(20),
                                      ' occupation': sql.types.String(20),
                                      ' relationship': sql.types.String(20),
                                      ' race': sql.types.String(12),
                                      ' sex': sql.types.String(10),
                                      ' capital-gain': sql.types.Integer,
                                      ' capital-loss': sql.types.Integer,
                                      ' hours-per-week': sql.types.Integer,
                                      ' native-country': sql.types.String(20),
                                      ' salary': sql.types.String(5)})
                eng.execute('ALTER TABLE `adults` ADD `id` INT NOT NULL AUTO_INCREMENT FIRST,'
                            ' ADD PRIMARY KEY (`id`);'
                            'ALTER TABLE `adults` ADD `native-country-trans` VARCHAR(20) '
                            'NULL DEFAULT NULL AFTER ` native-country`;')
            # query1
            successToString()
        else:
            print('Path does not exits')
    else:
        print("[ERROR] Syntax ERROR please check your option command enter ? for more help")


def welcome():
    need_table = input("welcome to rassam \n do you need create table ?(y/n) default n\n>")
    if need_table == "y":
        return adult()  # create adult table and add all cols - return false when no error occur
    else:
        print('that\'s ok!')
        return False
