import Manager
from pyactiveresource.connection import ResourceNotFound

shop_url = None
shop_token = None
while True:
    try:
        print(
        """\033[32m
         ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄    ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄     ▄▄▄▄▄▄▄ 
        █       █  █ █  █       █       █   █       █  █ █  █  █       █       █       █   █   █       █
        █  ▄▄▄▄▄█  █▄█  █   ▄   █    ▄  █   █    ▄▄▄█  █▄█  █  █▄     ▄█   ▄   █   ▄   █   █   █  ▄▄▄▄▄█
        █ █▄▄▄▄▄█       █  █ █  █   █▄█ █   █   █▄▄▄█       █    █   █ █  █ █  █  █ █  █   █   █ █▄▄▄▄▄ 
        █▄▄▄▄▄  █   ▄   █  █▄█  █    ▄▄▄█   █    ▄▄▄█▄     ▄█    █   █ █  █▄█  █  █▄█  █   █▄▄▄█▄▄▄▄▄  █
         ▄▄▄▄▄█ █  █ █  █       █   █   █   █   █     █   █      █   █ █       █       █       █▄▄▄▄▄█ █
        █▄▄▄▄▄▄▄█▄▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄█   █▄▄▄█▄▄▄█     █▄▄▄█      █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█                                               

        Bem-vindo !
        Pressione Ctrl + C para finalizar o programa a qualquer momento (evite pressionar durante a execução de uma função).
        Para o programa funcionar você precisa digitar algumas informações antes.
        Fique tranquilo, nenhuma informação fica salva.              
        """
        )

        if shop_url == None:
          shop_url = input("Url original da loja (Ex: myshop.myshopify.com): ")
          shop_token = input("Token de app (para obter crie um app com todas as permissões): ")

        try:
            session = Manager.Session(shop_token, shop_url)
            active_session = session.initStoreSession()
            if active_session is None:
                shop_url = None
                shop_token = None
                print("[Error] Loja não encontrada")
                continue
        except Exception as e:
            if not isinstance(e, ResourceNotFound):
                print(f"[Error] Verifique as informações e se a conexão com a internet está estável e tente novamente {e}")
                shop_url = None
                shop_token = None
                continue


        print(
        """
        [1] Atualizar preços de uma coleção                  [5] Atualizar comparação de preços de um produto                                              
        [2] Atualizar preços de um produto                   [6] Consultar produto pelo id
        [3] Consultar produtos de uma coleção                [7] Atualizar em massa estoque das variantes de um produto   
        [4] Atualizar comparações de preços de uma coleção   [8] Atualizar estoque de uma variante de um produto
        """    
        )
        option_selected = int(input("Digite o número correspondente a função desejada: "))

        if option_selected == 1: 
            try:
                collection_id = int(input("Id da coleção: "))
                print("[Alerta] Se negativa será subtraída do valor do produto, se positiva será acrescentada ao valor do produto")
                percentage_to_update = input("Porcentagem (Ex: -15.34%): ")
                collection = Manager.Collection(collection_id)
                collection.UpdateAllProductsPrices(percentage=float(percentage_to_update.strip('%')))
                input("Pressione Enter para continuar...")
            except:
                print(f"[Error] Coleção não encontrada ou não atualizada com sucesso")
                input("Pressione Enter para continuar...")
                continue
            
        if option_selected == 2:
            try:
                product_id = int(input("Id do produto: "))
                print("[Alerta] Se negativa será subtraída do valor do produto, se positiva será acrescentada ao valor do produto")
                percentage_to_update = input("Porcentagem (Ex: -15.34%): ")
                product = Manager.Product(product_id)
                product.UpdateAllVariantsPrices(percentage=float(percentage_to_update.strip('%')))
                input("Pressione Enter para continuar...")
            except:
                print("[Error] Produto não encontrado ou não atualizado com sucesso")
                input("Pressione Enter para continuar...")
                continue
            
        if option_selected == 3:
            try:
                collection_id = int(input("Id da coleção: "))
                collection = Manager.Collection(collection_id)
                collection.GetCollectionProducts()
                input("Pressione Enter para continuar...")
            except:
                print(f"[Error] Coleção não encontrada")
                input("Pressione Enter para continuar...")
                continue

        if option_selected == 4: 
            try:
                collection_id = int(input("Id da coleção: "))
                print("[Alerta] Se o preço de comparação de algum produto for igual a 0 ou estiver vazio ele passará a ser igual ao valor atual com a porcentagem a ser somada ou subtraida")
                print("[Alerta] Se negativa será subtraída do valor do produto, se positiva será acrescentada ao valor do produto")
                percentage_to_update = input("Porcentagem (Ex: -15.34%): ")
                collection = Manager.Collection(collection_id)
                collection.UpdateAllProductsComparePrices(percentage=float(percentage_to_update.strip('%')))
                input("Pressione Enter para continuar...")
            except:
                print(f"[Error] Coleção não encontrada ou não atualizada com sucesso")
                input("Pressione Enter para continuar...")
                continue
            
        if option_selected == 5: 
            try:
                product_id = int(input("Id do produto: "))
                print("[Alerta] Se o preço de comparação do produto for igual a 0 ou estiver vazio ele passará a ser igual ao valor atual com a porcentagem a ser somada ou subtraida")
                print("[Alerta] Se negativa será subtraída do valor do produto, se positiva será acrescentada ao valor do produto")
                percentage_to_update = input("Porcentagem (Ex: -15.34%): ")
                product = Manager.Product(product_id)
                product.UpdateAllVariantsComparePrices(percentage=float(percentage_to_update.strip('%')))
                input("Pressione Enter para continuar...")
            except:
                print("[Error] Produto não encontrado ou não atualizado com sucesso")
                input("Pressione Enter para continuar...")
                continue
            
        if option_selected == 6:
            try:
                product_id = int(input("Id do produto: "))
                product = Manager.Product(product_id)
                product.GetProduct()
                input("Pressione Enter para continuar...")
            except:
                print("[Error] Produto não encontrado")
                input("Pressione Enter para continuar...")
                continue

        if option_selected == 7:
            try:
                product_id = int(input("Id do produto: "))
                new_inventory = int(input("Nova quantidade em estoque: "))
                location_name = input("Nome da localização (como está na loja): ")
                product = session.UpdateVariantsInventory(newInventory=new_inventory, locationName=location_name, productId=product_id)
                input("Pressione Enter para continuar...")
            except:
                print(f"[Error] Produto não encontrado ou não atualizado com sucesso")
                input("Pressione Enter para continuar...")
                continue

        if option_selected == 8:
            try:
                variant_id = int(input("Id da variante: "))
                new_inventory = int(input("Nova quantidade em estoque: "))
                location_name = input("Nome da localização (como está na loja): ")
                session.UpdateVariantInventory(newInventory=new_inventory, locationName=location_name, variantId=variant_id)
                input("Pressione Enter para continuar...")
            except:
                print("[Error] Variante não encontrada ou não atualizada com sucesso")
                input("Pressione Enter para continuar...")
                continue
                
    except KeyboardInterrupt:
        print("\nPrograma finalizado\033[39m")
        break