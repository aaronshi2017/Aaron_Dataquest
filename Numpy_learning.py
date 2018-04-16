import numpy
world_alcohol=numpy.genfromtxt("world_alcohol.csv",delimiter=",",skip_header=1,dtype="U75")
countries_canada=world_alcohol[:,2]=="Canada"
years_1984=world_alcohol[:,0]=="1984"

country_is_algeria=world_alcohol[:,2]=="Algeria"
country_algeria=world_alcohol[country_is_algeria,:]

is_algeria_and_1986=(world_alcohol[:,0]=="1986")&(world_alcohol[:,2]=="Algeria")
rows_with_algeria_and_1986=world_alcohol[is_algeria_and_1986,:]

x=world_alcohol[:,0]=="1986"
y=world_alcohol[:,3]=="Wine"
world_alcohol[x,0]="2014"
world_alcohol[y,3]="Grog"

print(world_alcohol)

is_value_empty=world_alcohol[:,4]==''
world_alcohol[is_value_empty,4]="0"

print(world_alcohol)

alcohol_consumption=world_alcohol[:,4]
alcohol_consumption=alcohol_consumption.astype(float)
print(alcohol_consumption)

total_alcohol=alcohol_consumption.sum()
average_alcohol=alcohol_consumption.mean()

print(total_alcohol)
print(average_alcohol)

world_alcohol=numpy.genfromtxt("world_alcohol.csv",delimiter=",",skip_header=1,dtype="U75")
canada_1986=world_alcohol[(world_alcohol[:,0]=="1986") & (world_alcohol[:,2]=="Canada"),:]

canada_1986[canada_1986[:,4]=='',4]='0'
canada_alcohol=canada_1986[:,4].astype(float)
total_canadian_drinking=canada_alcohol.sum()
print(total_canadian_drinking)

countries=['Sierra Leone',
 'Namibia',
 'Hungary',
 'Brunei Darussalam',
 'Germany',
 'Pakistan',
 'Liberia',
 'Poland',
 'Cyprus',
 'Canada',
 'Morocco',
 'Greece',
 'Israel',
 'Egypt',
 'New Zealand',
 'Kiribati',
 'Nigeria',
 'Ghana',
 'Algeria',
 'Indonesia',
 'Bangladesh',
 'Seychelles',
 'China',
 'Netherlands',
 'Belarus',
 'Cambodia',
 'Saint Kitts and Nevis',
 'Lebanon',
 'Slovakia',
 'Norway',
 'Thailand',
 'Venezuela (Bolivarian Republic of)',
 'Belize',
 'Jamaica',
 'Sao Tome and Principe',
 'Trinidad and Tobago',
 "Cte d'Ivoire",
 'Slovenia',
 'Panama',
 'South Africa',
 'Republic of Korea',
 'Equatorial Guinea',
 'Swaziland',
 'Ethiopia',
 'Latvia',
 'Samoa',
 'Yemen',
 'Bhutan',
 'Libya',
 'Bolivia (Plurinational State of)',
 'Tunisia',
 'Australia',
 'France',
 "Democratic People's Republic of Korea",
 'Rwanda',
 'Ecuador',
 'Botswana',
 'Zambia',
 'Senegal',
 'Somalia',
 'Cabo Verde',
 'Fiji',
 'Lesotho',
 'Burundi',
 'Mali',
 'Guyana',
 'Jordan',
 'Chad',
 'United Kingdom of Great Britain and Northern Ireland',
 'Burkina Faso',
 'Kuwait',
 'Qatar',
 'Solomon Islands',
 'Romania',
 'Togo',
 'Vanuatu',
 'Nepal',
 'Antigua and Barbuda',
 'Micronesia (Federated States of)',
 'Portugal',
 'Belgium',
 'Bulgaria',
 'United Republic of Tanzania',
 'Saint Lucia',
 'Niger',
 'Iraq',
 'Malaysia',
 'Cuba',
 'Syrian Arab Republic',
 'Iceland',
 'Honduras',
 'Kenya',
 'Mauritania',
 'Austria',
 'Madagascar',
 'Mongolia',
 'Haiti',
 'Bahrain',
 'Czech Republic',
 'Spain',
 'Viet Nam',
 'Dominican Republic',
 'Eritrea',
 'Albania',
 'Guinea-Bissau',
 'El Salvador',
 'Italy',
 'Chile',
 'Russian Federation',
 'Oman',
 'Sudan',
 'Cameroon',
 'Peru',
 'Mozambique',
 'Denmark',
 'Bahamas',
 'Comoros',
 'Brazil',
 'Japan',
 'Iran (Islamic Republic of)',
 'Lithuania',
 'Ireland',
 'Turkey',
 'Kyrgyzstan',
 'Gabon',
 'Costa Rica',
 'Uganda',
 'Mexico',
 'Congo',
 'Guatemala',
 'Luxembourg',
 'Central African Republic',
 'Suriname',
 'Malawi',
 'Guinea',
 'Myanmar',
 'Democratic Republic of the Congo',
 'Malta',
 'Djibouti',
 "Lao People's Democratic Republic",
 'Mauritius',
 'Sweden',
 'India',
 'Argentina',
 'Switzerland',
 'Finland',
 'Zimbabwe',
 'Papua New Guinea',
 'Paraguay',
 'Singapore',
 'Afghanistan',
 'Saudi Arabia',
 'Angola',
 'Sri Lanka',
 'Ukraine',
 'Philippines',
 'Nicaragua',
 'Uruguay',
 'Gambia',
 'Colombia',
 'Benin',
 'United States of America',
 'Croatia',
 'United Arab Emirates']
totals = {}

for country in countries:
    countryrowcondition=(world_alcohol[:,2]==country)&(world_alcohol[:,0]=="1989")
    country_consumption=world_alcohol[countryrowcondition,:]
    country_consumption[country_consumption[:,4]=="",:]="0"
    x=country_consumption[:,4].astype(float)
    sumx=x.sum()
    totals[country]=sumx
print(totals)

highest_value = 0
highest_key = None

for country in totals:
    if totals[country]>highest_value:
        highest_key=country
        highest_value=totals[country]
print(highest_key)
print(highest_value)



