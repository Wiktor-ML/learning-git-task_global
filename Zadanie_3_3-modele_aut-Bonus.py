models = ['Volkswagen - Golf','Renault - Clio','Volkswagen - Polo',
'Ford - Fiesta','Nissan - Qashqai','Peugeot - 208','VW - Tiguan','Skoda - Octavia',
'Toyota - Yaris','Opel - Corsa','Dacia - Sandero','Renault - Captur','Citroen - C3',
'Peugeot - 3008','Ford - Focus','Fiat - 500','Dacia - Duster','Peugeot - 2008',
'Skoda - Fabia','Fiat - Panda','Opel - Astra','VW - Passat','Mercedes-Benz - A-Class',
'Peugeot - 308','Ford - Kuga']

sales2018 = ['445,754','336,268','299,920','270,738','233,026','230,049','224,788',
'223,352','217,642','217,036','216,306','214,720','210,082','204,197','196,583',
'191,205','182,100','180,204','172,511','168,697','160,275','157,986','156,020',
'155,925','154,125']

sales2017 = ['483,105','327,395','272,061','254,539','247,939','244,615','234,916',
'230,116','199,182','232,738','196,067','212,768','207,299','166,784','214,661',
'189,928','NA','180,868','180,136','187,322','217,813','184,123','NA','NA','NA']

sales2016 = ['492,952','315,115','308,561','300,528','234,340','249,047','180,198',
'230,255','193,969','264,844','170,300','217,105','134,560','NA','214,435',
'183,730','NA','NA','177,301','191,617','253,483','208,575','NA','195,653','NA']

answer1 = "" # wskaż nazwę modelu jako string
answer2 = "" # wskaż producenta jako string
answer3 = [] # wskaż odpowiedź jako listę zawierającą wszystkie modele spełniające kryteria
answer4 = "" # wskaż nazwę modelu jako string
answer5 = "" # odpowiedź podaj w formacie procentowym jako string. Np. '21%'

cars = {}
cars_1 = {item.split(' - ')[0]: item.split(' - ')[1] for item in models}

# Create a single dictionary with sales data for all years
cars = {}


    
for i, model in enumerate(models):
    manufacturer, car_model = model.split(' - ')
    # Initialize the manufacturer dictionary if it doesn't exist
    if manufacturer not in cars:
        cars[manufacturer] = {}

    # Add the car model data with 'sales' subdictionary
    # Convert sales numbers by removing commas and converting to integers
    cars[manufacturer][car_model] = {
        'sales': {
            '2016': int(sales2016[i].replace(',', '')) if sales2016[i] != 'NA' else 'NA',
            '2017': int(sales2017[i].replace(',', '')) if sales2017[i] != 'NA' else 'NA',
            '2018': int(sales2018[i].replace(',', ''))
        }
    }
#print(cars)

max_sales_2017 = 0
max_sales_2018 = 0
sales_2016_2017_2018 = 10000000000
answer_3 = []

for manufacturer in cars:
    for model in cars[manufacturer]:
        # Find the model with the biggest sales in 2017 (Answer 1)
        if cars[manufacturer][model]['sales']['2017'] != 'NA':
            if int(cars[manufacturer][model]['sales']['2017']) > max_sales_2017:
                max_sales_2017 = int(cars[manufacturer][model]['sales']['2017'])
                answer1_1= manufacturer
                answer1_2 = model
        
        # Find the model with the biggest sales in 2018 (Answer 2)
        if cars[manufacturer][model]['sales']['2018'] != 'NA': 
            if int(cars[manufacturer][model]['sales']['2018']) > max_sales_2018:
                max_sales_2018 = int(cars[manufacturer][model]['sales']['2018'])
                answer2_1= manufacturer
                answer2_2 = model
                
        # Find the model with no data for 2016 and was sold in 2017 (Answer 3)
        if cars[manufacturer][model]['sales']['2016'] == 'NA' and cars[manufacturer][model]['sales']['2017'] != 'NA':
            answer_3.append(f"{manufacturer} {model} has no data for 2016 and was sold in 2017") 
        
        # Calculate sales for 2016, 2017 and 2018 (Answer 4)
        if cars[manufacturer][model]['sales']['2016'] != 'NA':
            sales_2016 = int(cars[manufacturer][model]['sales']['2016'])
        else:
            sales_2016 = 0      
        if cars[manufacturer][model]['sales']['2017'] != 'NA':
            sales_2017 = int(cars[manufacturer][model]['sales']['2017'])
        else:
            sales_2017 = 0
        if cars[manufacturer][model]['sales']['2018'] != 'NA':
            sales_2018 = int(cars[manufacturer][model]['sales']['2018'])
        else:
            sales_2018 = 0
        # Add sales from 2016, 2017 and 2018 
        # Find the manufacturer with the lowest sales in 2016, 2017 and 2018
        if (sales_2016 + sales_2017 + sales_2018) < sales_2016_2017_2018:
            sales_2016_2017_2018 = sales_2016 + sales_2017 + sales_2018
            answer4_1 = manufacturer
            answer4_2 = model

# Increase of Ford sales between 2017 and 2018  (Answer 5)
sales_2017_ford = 0
sales_2018_ford = 0
for model in cars['Ford']:
    if cars['Ford'][model]['sales']['2017'] != 'NA':
        sales_2017_ford = sales_2017_ford + int(cars['Ford'][model]['sales']['2017'])
    if cars['Ford'][model]['sales']['2018'] != 'NA':
        sales_2018_ford = sales_2018_ford + int(cars['Ford'][model]['sales']['2018'])

increase_sales_ford = int((sales_2018_ford - sales_2017_ford) / sales_2017_ford * 100)
answer5 = increase_sales_ford

print(f"Answer 1: The biggest sales in 2017 had {answer1_1} with it's model {answer1_2}")   
print(f"Answer 2: The biggest sales in 2018 had {answer2_1} with it's model {answer2_2}")
print("Answer 3:") 
for item in answer_3:
    print(f"          {item}")
print(f"Answer 4: The manufacturer with the lowest sales in 2016, 2017 and 2018 is {answer4_1} with model {answer4_2}")
print(f"Answer 5: Increase of Ford sales between 2017 and 2018 is {answer5}%")
