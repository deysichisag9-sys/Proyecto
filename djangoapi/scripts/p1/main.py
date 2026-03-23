import sys

from parcelas.insert import insert as insert_parcelas
from parcelas.select import select as select_parcelas
from parcelas.update import update as update_parcelas
from parcelas.delete import delete as delete_parcelas 

def main():
    # sys.argv[0] es siempre el nombre del archivo (main.py)
    # Por eso verificamos que haya al menos 3 elementos (nombre + p1 + p2)
    if len(sys.argv) == 3:
        tableName = sys.argv[1]
        functionName = sys.argv[2]     
    else:
        print("Error: You mus give two parameters tableName and functionName to execute the addecuate function.")
        sys.exit(0)


    if tableName not in ["parcelas", "arboles", "caminos"]:
        print("Error: The available table names are parcelas, arboles, caminos")
        sys.exit(0)
    
    if functionName not in ["insert", "select", "selectAsDict", "update", "delete"]:
        print("Error the available function names are insert, select, delete or update")
        sys.exit(0)

    if tableName == "parcelas":
        if functionName=="insert":
            insert_parcelas()
        elif functionName=="select":
            select_parcelas()
        elif functionName=="selectAsDict":
            select_parcelas(asDict=True)
        elif functionName=="update":
            update_parcelas()
        elif functionName=="delete":
            delete_parcelas()
            
    elif tableName=="arboles":
        if functionName=="insert":
            pass
        elif functionName=="select":
            pass
        elif functionName=="update":
            pass
        elif functionName=="delete":
            pass

    elif tableName == "caminos":
        if functionName == "insert":
            pass 
        elif functionName == "select":
            pass
        elif functionName == "selectAsDict":
            pass
        elif functionName == "update":
            pass
        elif functionName == "delete":
            pass

if __name__ == "__main__":
    main()

