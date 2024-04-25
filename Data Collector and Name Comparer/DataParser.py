import pandas as pd

excel_file_path = "March Madness Basketball Data.xlsx"
years = ["2024", "2023", "2022", "2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007", "2006", "2005", "2004", "2003", "2002"]
#header = ["Name", "Seed", "W-L", "AdjEM", "AdjO", "AdjO Rank", "AdjD", "AdjD Rank", "AdjT", "AdjT Rank", "Luck", "Luck Rank", "SOS AdjEM", "SOS AdjEM Rank", "OppO", "OppO Rank", "OppD", "OppD Rank", "NCSOS AdjEM", "NCSOS AdjEM Rank"]

# with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='w') as writer:
    for year in years:
        file_path = year + " Pomeroy College Basketball Ratings.txt"
        rows = []
        with open(file_path, 'r') as file:
            for line in file:
                hold = line.strip()
                if '<td class="hard_left">' in hold and hold.count('<span class="seed">') == 9:
                    rows.append(hold)

        load = []
        for row in rows:
            hold = []
            count = 0
            word = ""
            for c in row:
                if c == '<':
                    if word.strip() != '': hold.append(word)
                    word = ""
                    count -= 1
                    continue
                elif c == '>':
                    count += 1
                    continue
                if count == 0:
                    word += c
            temp = [hold[1], float(hold[6]), float(hold[8])]
            load.append(temp)
            
        df = pd.DataFrame(load)
        df.to_excel(writer, sheet_name=year, index=False)
