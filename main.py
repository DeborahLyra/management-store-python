
import operator

initial_stock = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Mechanical Keyboard Corsair;207;30;180.00;300.00#Mechanical Keyboard Razer;208;25;200.00;350.00#HP Printer;209;5;400.00;650.00#Epson Printer;210;3;450.00;700.00#Dell Monitor;211;12;850.00;1250.00#AOC Monitor;212;7;700.00;1100.00"

#2
def add_initial_stock(stock_str):
    """
    Converte uma string de produtos formatados em uma lista de dicionários contendo os detalhes dos produtos.

    Args:
        stock_str (str): A string contendo os produtos, separados por '#', e suas propriedades separadas por ';'.

    Returns:
        list: Uma lista de dicionários representando os produtos.
    """
    products_list = []
    items = stock_str.split("#") #dividir pelo # para separar os produtos
    for item in items:
        description, code, quantity, cost, sale_price = item.split(";") #pesquisei e isso se chama  desempacotamento de tupla, vai arrastar os valores para as variaveis dividas pelo ;
        product = {
            "description": description,
            "code": int(code),
            "quantity": int(quantity),
            "cost": float(cost),
            "sale_price": float(sale_price) #transformar para números - fazer contas
        }
        products_list.append(product)
    return products_list

#1
def add_new_product(products, description, code, quantity, cost, sale_price):
    """
    Adiciona um novo produto à lista de produtos, verificando se o código já existe.

    Args:
        products (list): A lista atual de produtos.
        description (str): A descrição do novo produto.
        code (int): O código único do produto.
        quantity (int): A quantidade inicial em estoque.
        cost (float): O custo de compra do produto.
        sale_price (float): O preço de venda do produto.

    Returns:
        None
    """
    for product in products:
        #verificar se o código do produto já existe, se já existir, faz o return
        if product['code'] == code:
            print(f"The code already exists")
            return
    new_product = {
        "description": description,
        "code": code,
        "quantity": quantity,
        "cost": cost,
        "sale_price": sale_price
    }
    products.append(new_product)
    print(f"Product {description} added successfully!")

#3
def list_all_products(products):
    """
    Exibe todos os produtos presentes na lista de produtos.

    Args:
        products (list): A lista de produtos.

    Returns:
        None
    """
    for product in products:
        print(product)
        
#4
def order_by_quantity(products):
    """
    Ordena os produtos em ordem decrescente de quantidade em estoque e os exibe.

    Args:
        products (list): A lista de produtos.

    Returns:
        None
    """
    products_to_order = sorted(products, key=operator.itemgetter('quantity'), reverse=True) #operator.itemgetter para acessar a chave 'quantity'
    print(products_to_order)

#6
def search_product(product_info, products):
    """
    Procura um produto na lista de produtos pelo nome ou código.

    Args:
        product_info (str): O nome ou código do produto.
        products (list): A lista de produtos.

    Returns:
        None
    """
    for product in products:
        if product['description'].lower() == product_info.lower() or str(product['code']) == product_info:
            print(product)
    print('Product not found')
    return None

#7
def delete_product(product_to_delete, products):
    """
    Remove um produto da lista de produtos pelo código.

    Args:
        product_to_delete (str): O código do produto a ser removido.
        products (list): A lista de produtos.

    Returns:
        None
    """
    for product in products:
        if str(product['code']) == product_to_delete:
            products.remove(product)
            print("Deleted successfully!")
            return
    print("Product not found")
    
#8
def sold_out_products(products):
    """
    Exibe os produtos que estão esgotados (quantidade igual a zero).

    Args:
        products (list): A lista de produtos.

    Returns:
        None
    """
    sold_out = []
    for product in products:
        if product['quantity'] == 0:
            sold_out.append(product)
            print(sold_out)
            return 
    print("None product sold out")

#9
def low_stock(products, quantity = 5):
    """
    Exibe os produtos que têm estoque abaixo de uma quantidade especificada.

    Args:
        products (list): A lista de produtos.
        quantity (int): A quantidade limite para considerar baixo estoque (padrão é 5).

    Returns:
        None
    """
    low_stock_quantity = []
    for product in products:
        if product['quantity'] < quantity:
            low_stock_quantity.append(product)

    if low_stock_quantity:
        print("Products with low stock:")
        for product in low_stock_quantity:
            print(product)
    else:
        print("Everything is filled up")

#10
def update_stock(add_or_sell, product_code, quantity, products):
    """
    Atualiza o estoque de um produto adicionando ou vendendo unidades.

    Args:
        add_or_sell (str): Operação de adicionar ('add') ou vender ('sell').
        product_code (int): O código do produto.
        quantity (int): A quantidade a ser adicionada ou vendida.
        products (list): A lista de produtos.

    Returns:
        None
    """
    for product in products:
        if product['code'] == product_code:    
            if add_or_sell == 'add':    
                product['quantity'] += quantity    
            elif add_or_sell == 'sell':
                 product['quantity'] -= quantity 
            else:
                print("Something went wrong")
                return
            print(f"Stock updated successfully!")
            return    
    print(f"Product with code {product_code} not found.")

#11 
def change_price(products, new_price, product_code):
    """
    Altera o preço de venda de um produto.

    Args:
        products (list): A lista de produtos.
        new_price (float): O novo preço de venda.
        product_code (int): O código do produto.

    Returns:
        None
    """
    for product in products:
        if product['code'] == product_code:
            product['sale_price'] = new_price
            print(f"Price updated successfully!")
            return 
    print(f"Product with code {product_code} not found.")

#12
def check_values(product, quantity=0, price=None):
    """
    Calcula e exibe o valor total de cada produto em estoque.

    Args:
        products (list): A lista de produtos.

    Returns:
        None
    """
    if product['quantity'] + quantity < 0:
        print("Error: Stock can't be negative.")
        return False

    if price is not None and price < product['cost']:
        print("Sale price can't be lower than the cost.")
        return False

    return True
    
#13
def calculate_total_stock(products):
    """
    Calcula e exibe o lucro presumido de cada produto, com base no custo e preço de venda.

    Args:
        products (list): A lista de produtos.

    Returns:
        None
    """
    for product in products:
        total_stock = product['quantity'] * product['sale_price']
        print(f"\nThe total price in the stock of {product['description']} is {int(total_stock)}")    

#14
def presumed_profit(products):
    """
    Gera um relatório de estoque, exibindo descrição, código, quantidade, custo, preço de venda e valor total por produto.

    Args:
        products (list): A lista de produtos.

    Returns:
        None
    """
    for product in products:
        profit = product['quantity'] * (product['sale_price'] - product['cost'])
        print(f"\nThe profit of {product['description']} is {int(profit)}")

#16
def generate_stock_report(products):
    """
    Gera um relatório de estoque, exibindo descrição, código, quantidade, custo, preço de venda e valor total por produto.

    Args:
        products (list): A lista de produtos.

    Returns:
        None
    """
    print(f"{'Description'.ljust(30)}{'Code'.rjust(6)}{'Qantity'.rjust(6)}{'Cost'.rjust(12)}{'Sale Price'.rjust(15)}{'Total Value'.rjust(15)}")
    print("-" * 84)

    total_cost = 0
    total_revenue = 0

    for product in products:
        description = product['description'].ljust(30)
        code = str(product['code']).rjust(6)
        quantity = str(product['quantity']).rjust(6)
        cost = f"{product['cost']:.2f}".rjust(12)
        sale_price = f"{product['sale_price']:.2f}".rjust(15)
        total_value = f"{product['quantity'] * product['sale_price']:.2f}".rjust(15)

        # paramostar a linha formatada
        print(f"{description}{code}{quantity}{cost}{sale_price}{total_value}")

        # somar ao custo total e faturamento total
        total_cost += product['quantity'] * product['cost']
        total_revenue += product['quantity'] * product['sale_price']

    print("-" * 84)
    print(f"{'Total Cost:'.ljust(69)}{f'{total_cost:.2f}'.rjust(15)}")
    print(f"{'Total Revenue:'.ljust(69)}{f'{total_revenue:.2f}'.rjust(15)}")



initial_products = add_initial_stock(initial_stock)

#5
def menu():
    print("\n=== Product Management Menu ===")
    print("1. List all products")
    print("2. Add a new product")
    print("3. Order products by quantity")
    print("4. Search for a product")
    print("5. Delete a product")
    print("6. Show sold out products")
    print("7. Show low stock products")
    print("8. Update stock")
    print("9. Change product price")
    print("10. Calculate total stock value")
    print("11. Calculate presumed profit")
    print("12. Generate stock report")
    print("13. Exit")
    return input("Choose an option: ")

def main():
    products = add_initial_stock(initial_stock)

    while True:
        option = menu()

        if option == "1":
            list_all_products(products)
        elif option == "2":
            description = input("Enter description: ")
            code = int(input("Enter code: "))
            quantity = int(input("Enter quantity: "))
            cost = float(input("Enter cost: "))
            sale_price = float(input("Enter sale price: "))
            add_new_product(products, description, code, quantity, cost, sale_price)
        
        elif option == "3":
            order_by_quantity(products)
        
        elif option == "4":
            product_info = input("Enter product name or code: ")
            search_product(product_info, products)
        
        elif option == "5":
            product_to_delete = input("Enter product code to delete: ")
            delete_product(product_to_delete, products)
        
        elif option == "6":
            sold_out_products(products)
        
        elif option == "7":
            threshold = int(input("If you want, type a minum quantity (default value: 5): "))
            low_stock(products, threshold)
        elif option == "8":
            add_or_sell = input("Do you want to 'add' or 'sell' a product?: ")
            product_code = int(input("Enter product code: "))
            quantity = int(input("Enter quantity: "))
            for product in products:
                #checar se o valor passado é válido segundo exigido 
                if product['code'] == product_code:
                    if check_values(product, quantity):
                        update_stock(add_or_sell, product_code, quantity, products)
                    break
            else:
                print(f"Product with code {product_code} not found.")
       
        elif option == "9":
            product_code = int(input("Enter product code: "))
            new_price = float(input("Enter new sale price: "))
            for product in products:
                if product['code'] == product_code:
                    if check_values(product, price=new_price):
                        change_price(products, new_price, product_code)
                    break
            else:
                print(f"Product with code {product_code} not found.")
        
        elif option == "10":
            calculate_total_stock(products)
        
        elif option == "11":
            presumed_profit(products)
        
        elif option == "12":
            generate_stock_report(products)
        
        elif option == "13":
            print("Exiting...")
            break
        
        else:
            print("Invalid option")

main()
