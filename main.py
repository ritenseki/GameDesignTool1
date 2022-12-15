import pandas as pd
file_path = '第一、二时代.xlsx'
generationOne = pd.read_excel(file_path, sheet_name="Sheet1", header=None)
generationTwo = pd.read_excel(file_path, sheet_name="Sheet2", header=None)

#print(generationOne)
#print(generationTwo)
#print()



datas = [generationOne, generationTwo]
generation =1
for data in datas:
    print(data)
    lines = data.shape[0]
    columns = data.shape[1]
    readingLines = 1
    while readingLines + 1 <= lines:
        readingColumns = 0
        printingList = []
        while readingColumns + 1 <= columns-4:
            name = data.iloc[0,readingColumns]
            value = data.iloc[readingLines,readingColumns]
            if value != 0:
                printingList.append(r'{}:{}'.format(name,value))
            readingColumns += 1

        #item = data.iloc[readingLines,columns-1]
        data.loc[readingLines,columns+1] = ' '.join(printingList)
        #print(data)
        data.to_excel(f'输出{str(generation)}.xlsx', header=None, index=None)
        readingLines += 1
    generation+=1