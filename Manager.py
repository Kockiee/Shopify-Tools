import json
from prettytable import PrettyTable
from prettytable import ALL as prettytable_all_rules
import shopify
from pyactiveresource.connection import ResourceNotFound
from time import sleep

def getCollectionJsonData(collectionId):
    try:
        response = shopify.CustomCollection.find(collectionId)
        return response
    except Exception as e:
        if isinstance(e, ResourceNotFound):
            try:
                response = shopify.SmartCollection.find(collectionId)
                return response
            except Exception as e:
                raise ResourceNotFound

def getLocationIdByName(locationName):
    locations = shopify.Location.find()

    for location in locations:
        if location.name == locationName:
            return location.id
    return None

# // Session Class //

class Session():
    def __init__(self, token, store_url):
        self.token = token
        self.store_url = store_url
        self.session = shopify.Session(self.store_url, version="2023-10", token=self.token)
    
    def initStoreSession(self):
        try:
            shopify.ShopifyResource.activate_session(self.session)
            store = shopify.Shop.current()
            return store
        except ResourceNotFound:
            return None
        
    def UpdateVariantsInventory(self, newInventory, locationName, productId):
        if not newInventory < 0:
            product = shopify.Product.find(productId)

            location_id = getLocationIdByName(locationName)

            for variant in product.variants:
                print(f"Atualizando o estoque da variante {variant.title} para {newInventory}")
                
                inventory_level = shopify.InventoryLevel()
                inventory_level.set(inventory_item_id=variant.inventory_item_id, location_id=location_id, available=newInventory)
                sleep(1)
            print("Quantidades atualizadas com sucesso")
        else:
            print("A nova quantidade em estoque não pode ser negativa")
    
    def UpdateVariantInventory(self, newInventory, locationName, variantId):
        if not newInventory < 0:
            variant = shopify.Variant.find(variantId)

            location_id = getLocationIdByName(locationName)

            print(f"Atualizando o estoque da variante {variant.title} para {newInventory}")

            inventory_level = shopify.InventoryLevel()
            inventory_level.set(inventory_item_id=variant.inventory_item_id, location_id=location_id, available=newInventory)
            print("Estoque atualizado com sucesso")
        else:
            print("A nova quantidade em estoque não pode ser negativa")

# // Collection Class //

class Collection():
    def __init__(self, id):
        self.collection_id = id
    
    def GetCollectionProducts(self):
        collection = getCollectionJsonData(self.collection_id)

        products = collection.products()

        table = PrettyTable()
        table.title = 'Informações do produto'
        table.field_names = ["Id", "Título do Produto", "Handle do produto", "Url da imagem principal", "Data de criação"]
        table.align = 'l'
        table._max_width = {"Id": 12, "Título do Produto": 20, "Handle do produto": 20, "Url da imagem principal": 50, "Data de criação": 20}

        for product in products:
            table.add_row([product.id, product.title, product.handle, product.images[0].src, product.created_at])

        table.hrules = prettytable_all_rules
        print(table)

    def UpdateAllProductsPrices(self, percentage):
        if not percentage == 0:
            collection = getCollectionJsonData(self.collection_id)

            products = collection.products()

            for product in products:
                print(f'{"Aumentando" if percentage > 0 else "Reduzindo"} em {percentage}% o preço das variantes do produto "{product.title}"')
                for variant in product.variants:
                    price = float(variant.price)
                    variant.price = price + ((price * percentage) / 100)
                    variant.save()
                    sleep(1)

            print("Operação concluída com êxito")
        else:
            print("A porcentagem passada não pode ser igual a 0, tente novamente")
    
    def UpdateAllProductsComparePrices(self, percentage):
        collection = getCollectionJsonData(self.collection_id)
        products = collection.products()

        for product in products:
            print(f'{"Aumentando" if percentage > 0 else "Reduzindo"} em {percentage}% o preço de comparação das variantes do produto "{product.title}"')

            for variant in product.variants:
                price = float(variant.price)
                compare_at_price = float(variant.compare_at_price)

                if variant.compare_at_price is not None and compare_at_price != 0:
                    variant.compare_at_price = compare_at_price + ((compare_at_price * percentage) / 100) 
                else:
                    variant.compare_at_price = price + ((price * percentage) / 100)

                variant.save()
                sleep(1)
        print("Operação concluída com êxito")

# // Product Class //

class Product():
    def __init__(self, id):
        self.product_id = id

    def GetProduct(self):
        product = shopify.Product.find(self.product_id)
        product_table = PrettyTable()
        product_table.title = 'Informações do produto'
        product_table.field_names = ["Id", "Título do Produto", "Handle do produto", "Url da imagem principal", "Data de criação"]
        product_table.align = 'l'
        product_table._max_width = {"Id": 12, "Título do Produto": 20, "Handle do produto": 20, "Url da imagem principal": 50, "Data de criação": 20}
        product_table.add_row([product.id, product.title, product.handle, product.images[0].src, product.created_at])
        product_table.hrules = prettytable_all_rules
        print(product_table)
        
        variants_table = PrettyTable()
        variants_table.title = 'Variantes do produto'
        variants_table.field_names = ["Id", "Título da variante", "Preço", "Preço de comparação", "Data de criação"]
        variants_table.align = 'l'
        variants_table._max_width = {"Id": 12, "Título da variante": 20, "Preço": 10, "Preço de comparação": 10, "Data de criação": 20}

        for variant in product.variants:
            variants_table.add_row([variant.id, variant.title, variant.price, variant.compare_at_price, variant.created_at])
        variants_table.hrules = prettytable_all_rules

        print(variants_table)

        print(json.dumps(product.to_dict(), indent=2))
    
    def UpdateAllVariantsPrices(self, percentage):
        if not percentage == 0:
            product = shopify.Product.find(self.product_id)

            print(f'{"Aumentando" if percentage > 0 else "Reduzindo"} em {percentage}% o preço das variantes do produto "{product.title}"')

            for variant in product.variants:
                price = float(variant.price)
                variant.price = price + ((price * percentage) / 100)
                variant.save()
                sleep(1)

            print("Operação concluída com êxito")
        else:
            print("A porcentagem passada não pode ser igual a 0, tente novamente")

    def UpdateAllVariantsComparePrices(self, percentage):
        product = shopify.Product.find(self.product_id)

        print(f'{"Aumentando" if percentage > 0 else "Reduzindo"} em {percentage}% o preço de comparação das variantes do produto "{product.title}"...')

        for variant in product.variants:
            price = float(variant.price)
            compare_at_price = float(variant.compare_at_price)

            if variant.compare_at_price is not None and compare_at_price != 0:
                variant.compare_at_price = compare_at_price + ((compare_at_price * percentage) / 100) 
            else:
                variant.compare_at_price = price + ((price * percentage) / 100)

            variant.save()
            sleep(1)

            print(f"Variante {variant.title} atualizada")

        print("Operação concluída com êxito")