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
        add(1)
        # query
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

