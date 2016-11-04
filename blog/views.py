# History
#
# 2016-08-09 Add PhotoIndex

# System imports
import operator
from django.db.models import Q

from django.shortcuts import render
from django.views import generic

import plotly.offline as opy
import plotly.graph_objs as go

import pandas as pd

from . import models

class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 5

class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"

class WebsiteIndex(generic.ListView):
    queryset = models.Website.objects.published()
    template_name = "website.html"

class ProjectIndex(generic.ListView):
    queryset = models.Project.objects.published()
    template_name = "project.html"

class PhotoIndex(generic.ListView):
    queryset = models.Photoset.objects.all()
    template_name = "photo.html"

class Graph(generic.TemplateView):
    template_name = 'graph.html'

    def get_context_data(self, **kwargs):
        context = super(Graph, self).get_context_data(**kwargs)
        country_data = [[u'Afghanistan', u'AFG', 0], [u'\xc5land Islands', u'ALA', 0], [u'Albania', u'ALB', 0], [u'Algeria', u'DZA', 0], [u'American Samoa', u'ASM', 0], [u'Andorra', u'AND', 0], [u'Angola', u'AGO', 0], [u'Anguilla', u'AIA', 0], [u'Antarctica', u'ATA', 0], [u'Antigua and Barbuda', u'ATG', 0], [u'Argentina', u'ARG', 0], [u'Armenia', u'ARM', 0], [u'Aruba', u'ABW', 0], [u'Australia', u'AUS', 1], [u'Austria', u'AUT', 0], [u'Azerbaijan', u'AZE', 0], [u'Bahamas', u'BHS', 0], [u'Bahrain', u'BHR', 0], [u'Bangladesh', u'BGD', 0], [u'Barbados', u'BRB', 0], [u'Belarus', u'BLR', 0], [u'Belgium', u'BEL', 0], [u'Belize', u'BLZ', 0], [u'Benin', u'BEN', 0], [u'Bermuda', u'BMU', 0], [u'Bhutan', u'BTN', 0], [u'Bolivia, Plurinational State of', u'BOL', 0], [u'Bonaire, Sint Eustatius and Saba', u'BES', 0], [u'Bosnia and Herzegovina', u'BIH', 0], [u'Botswana', u'BWA', 0], [u'Bouvet Island', u'BVT', 0], [u'Brazil', u'BRA', 0], [u'British Indian Ocean Territory', u'IOT', 0], [u'Brunei Darussalam', u'BRN', 0], [u'Bulgaria', u'BGR', 0], [u'Burkina Faso', u'BFA', 0], [u'Burundi', u'BDI', 0], [u'Cambodia', u'KHM', 0], [u'Cameroon', u'CMR', 0], [u'Canada', u'CAN', 0], [u'Cape Verde', u'CPV', 0], [u'Cayman Islands', u'CYM', 0], [u'Central African Republic', u'CAF', 0], [u'Chad', u'TCD', 0], [u'Chile', u'CHL', 0], [u'China', u'CHN', 0], [u'Christmas Island', u'CXR', 0], [u'Cocos (Keeling) Islands', u'CCK', 0], [u'Colombia', u'COL', 0], [u'Comoros', u'COM', 0], [u'Congo', u'COG', 0], [u'Congo, The Democratic Republic of the', u'COD', 0], [u'Cook Islands', u'COK', 0], [u'Costa Rica', u'CRI', 0], [u"C\xf4te d'Ivoire", u'CIV', 0], [u'Croatia', u'HRV', 0], [u'Cuba', u'CUB', 0], [u'Cura\xe7ao', u'CUW', 0], [u'Cyprus', u'CYP', 0], [u'Czech Republic', u'CZE', 0], [u'Denmark', u'DNK', 0], [u'Djibouti', u'DJI', 0], [u'Dominica', u'DMA', 0], [u'Dominican Republic', u'DOM', 0], [u'Ecuador', u'ECU', 0], [u'Egypt', u'EGY', 0], [u'El Salvador', u'SLV', 0], [u'Equatorial Guinea', u'GNQ', 0], [u'Eritrea', u'ERI', 0], [u'Estonia', u'EST', 0], [u'Ethiopia', u'ETH', 0], [u'Falkland Islands (Malvinas)', u'FLK', 0], [u'Faroe Islands', u'FRO', 0], [u'Fiji', u'FJI', 0], [u'Finland', u'FIN', 0], [u'France', u'FRA', 0], [u'French Guiana', u'GUF', 0], [u'French Polynesia', u'PYF', 0], [u'French Southern Territories', u'ATF', 0], [u'Gabon', u'GAB', 0], [u'Gambia', u'GMB', 0], [u'Georgia', u'GEO', 0], [u'Germany', u'DEU', 0], [u'Ghana', u'GHA', 0], [u'Gibraltar', u'GIB', 0], [u'Greece', u'GRC', 0], [u'Greenland', u'GRL', 0], [u'Grenada', u'GRD', 0], [u'Guadeloupe', u'GLP', 0], [u'Guam', u'GUM', 0], [u'Guatemala', u'GTM', 0], [u'Guernsey', u'GGY', 0], [u'Guinea', u'GIN', 0], [u'Guinea-Bissau', u'GNB', 0], [u'Guyana', u'GUY', 0], [u'Haiti', u'HTI', 0], [u'Heard Island and McDonald Islands', u'HMD', 0], [u'Holy See (Vatican City State)', u'VAT', 0], [u'Honduras', u'HND', 0], [u'Hong Kong', u'HKG', 0], [u'Hungary', u'HUN', 0], [u'Iceland', u'ISL', 0], [u'India', u'IND', 0], [u'Indonesia', u'IDN', 0], [u'Iran, Islamic Republic of', u'IRN', 0], [u'Iraq', u'IRQ', 0], [u'Ireland', u'IRL', 0], [u'Isle of Man', u'IMN', 0], [u'Israel', u'ISR', 0], [u'Italy', u'ITA', 0], [u'Jamaica', u'JAM', 0], [u'Japan', u'JPN', 1], [u'Jersey', u'JEY', 0], [u'Jordan', u'JOR', 0], [u'Kazakhstan', u'KAZ', 0], [u'Kenya', u'KEN', 0], [u'Kiribati', u'KIR', 0], [u"Korea, Democratic People's Republic of", u'PRK', 0], [u'Korea, Republic of', u'KOR', 16], [u'Kuwait', u'KWT', 0], [u'Kyrgyzstan', u'KGZ', 0], [u"Lao People's Democratic Republic", u'LAO', 0], [u'Latvia', u'LVA', 0], [u'Lebanon', u'LBN', 0], [u'Lesotho', u'LSO', 0], [u'Liberia', u'LBR', 0], [u'Libya', u'LBY', 0], [u'Liechtenstein', u'LIE', 0], [u'Lithuania', u'LTU', 0], [u'Luxembourg', u'LUX', 0], [u'Macao', u'MAC', 0], [u'Macedonia, Republic of', u'MKD', 0], [u'Madagascar', u'MDG', 0], [u'Malawi', u'MWI', 0], [u'Malaysia', u'MYS', 0], [u'Maldives', u'MDV', 0], [u'Mali', u'MLI', 0], [u'Malta', u'MLT', 0], [u'Marshall Islands', u'MHL', 0], [u'Martinique', u'MTQ', 0], [u'Mauritania', u'MRT', 0], [u'Mauritius', u'MUS', 0], [u'Mayotte', u'MYT', 0], [u'Mexico', u'MEX', 0], [u'Micronesia, Federated States of', u'FSM', 0], [u'Moldova, Republic of', u'MDA', 0], [u'Monaco', u'MCO', 0], [u'Mongolia', u'MNG', 0], [u'Montenegro', u'MNE', 0], [u'Montserrat', u'MSR', 0], [u'Morocco', u'MAR', 0], [u'Mozambique', u'MOZ', 0], [u'Myanmar', u'MMR', 0], [u'Namibia', u'NAM', 0], [u'Nauru', u'NRU', 0], [u'Nepal', u'NPL', 0], [u'Netherlands', u'NLD', 0], [u'New Caledonia', u'NCL', 0], [u'New Zealand', u'NZL', 0], [u'Nicaragua', u'NIC', 0], [u'Niger', u'NER', 0], [u'Nigeria', u'NGA', 0], [u'Niue', u'NIU', 0], [u'Norfolk Island', u'NFK', 0], [u'Northern Mariana Islands', u'MNP', 0], [u'Norway', u'NOR', 0], [u'Oman', u'OMN', 0], [u'Pakistan', u'PAK', 0], [u'Palau', u'PLW', 0], [u'Palestine, State of', u'PSE', 0], [u'Panama', u'PAN', 0], [u'Papua New Guinea', u'PNG', 0], [u'Paraguay', u'PRY', 0], [u'Peru', u'PER', 0], [u'Philippines', u'PHL', 0], [u'Pitcairn', u'PCN', 0], [u'Poland', u'POL', 0], [u'Portugal', u'PRT', 0], [u'Puerto Rico', u'PRI', 0], [u'Qatar', u'QAT', 0], [u'R\xe9union', u'REU', 0], [u'Romania', u'ROU', 0], [u'Russian Federation', u'RUS', 0], [u'Rwanda', u'RWA', 0], [u'Saint Barth\xe9lemy', u'BLM', 0], [u'Saint Helena, Ascension and Tristan da Cunha', u'SHN', 0], [u'Saint Kitts and Nevis', u'KNA', 0], [u'Saint Lucia', u'LCA', 0], [u'Saint Martin (French part)', u'MAF', 0], [u'Saint Pierre and Miquelon', u'SPM', 0], [u'Saint Vincent and the Grenadines', u'VCT', 0], [u'Samoa', u'WSM', 0], [u'San Marino', u'SMR', 0], [u'Sao Tome and Principe', u'STP', 0], [u'Saudi Arabia', u'SAU', 0], [u'Senegal', u'SEN', 0], [u'Serbia', u'SRB', 0], [u'Seychelles', u'SYC', 0], [u'Sierra Leone', u'SLE', 0], [u'Singapore', u'SGP', 0], [u'Sint Maarten (Dutch part)', u'SXM', 0], [u'Slovakia', u'SVK', 0], [u'Slovenia', u'SVN', 0], [u'Solomon Islands', u'SLB', 0], [u'Somalia', u'SOM', 0], [u'South Africa', u'ZAF', 0], [u'South Georgia and the South Sandwich Islands', u'SGS', 0], [u'Spain', u'ESP', 0], [u'Sri Lanka', u'LKA', 0], [u'Sudan', u'SDN', 0], [u'Suriname', u'SUR', 0], [u'South Sudan', u'SSD', 0], [u'Svalbard and Jan Mayen', u'SJM', 0], [u'Swaziland', u'SWZ', 0], [u'Sweden', u'SWE', 0], [u'Switzerland', u'CHE', 0], [u'Syrian Arab Republic', u'SYR', 0], [u'Taiwan, Province of China', u'TWN', 0], [u'Tajikistan', u'TJK', 0], [u'Tanzania, United Republic of', u'TZA', 0], [u'Thailand', u'THA', 0], [u'Timor-Leste', u'TLS', 0], [u'Togo', u'TGO', 0], [u'Tokelau', u'TKL', 0], [u'Tonga', u'TON', 0], [u'Trinidad and Tobago', u'TTO', 0], [u'Tunisia', u'TUN', 0], [u'Turkey', u'TUR', 0], [u'Turkmenistan', u'TKM', 0], [u'Turks and Caicos Islands', u'TCA', 0], [u'Tuvalu', u'TUV', 0], [u'Uganda', u'UGA', 0], [u'Ukraine', u'UKR', 0], [u'United Arab Emirates', u'ARE', 0], [u'United Kingdom', u'GBR', 5], [u'United States', u'USA', 8], [u'United States Minor Outlying Islands', u'UMI', 0], [u'Uruguay', u'URY', 0], [u'Uzbekistan', u'UZB', 0], [u'Vanuatu', u'VUT', 0], [u'Venezuela, Bolivarian Republic of', u'VEN', 0], [u'Viet Nam', u'VNM', 0], [u'Virgin Islands, British', u'VGB', 0], [u'Virgin Islands, U.S.', u'VIR', 0], [u'Wallis and Futuna', u'WLF', 0], [u'Western Sahara', u'ESH', 0], [u'Yemen', u'YEM', 0], [u'Zambia', u'ZMB', 0], [u'Zimbabwe', u'ZWE', 0]]
        df = pd.DataFrame(country_data, columns=['Country name', 'Code', 'Amount'])

        #df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')

        data = [ dict(
                type = 'choropleth',
                locations = df['Code'],
                z = df['Amount'],
                text = df['Country name'],
                colorscale = [[0,"rgb(0, 228, 97)"], 
                              [0.35,"rgb(70, 232, 117)"],
                              [0.5,"rgb(100, 236, 138)"],
                              [0.6,"rgb(120, 240, 172)"],
                              [0.7,"rgb(140, 245, 201)"],
                              [1,"rgb(250, 250, 250)"]],
                autocolorscale = False,
                reversescale = True,
                marker = dict(
                    line = dict (
                        color = 'rgb(180,180,180)',
                        width = 0.5
                    )
                ),
                tick0 = 0,
                zmin = 0,
                dtick = 1000,
                colorbar = dict(
                    autotick = False,
                    tickprefix = '',
                    title = 'Number of artists'
                ),
            ) ]
        
        layout = dict(
            title = "Country of origin of artists I listen on Spotify",
            geo = dict(
                showframe = False,
                showcoastlines = False,
                projection = dict(
                    type = 'Mercator'
                )
            )
        )
        figure = dict(data=data, layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div', validate=False)

        context['graph'] = div

        return context
        
def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        queryset = models.Entry.objects.order_by('-created')
        query = request.GET['q']
        query_list = query.split()
        queryset = queryset.filter(
            reduce(operator.and_,
                   (Q(title__icontains=q) for q in query_list)) |
            reduce(operator.and_,
                   (Q(body__icontains=q) for q in query_list))
        )
        return render(request, 'search.html', { 'query_string': query, 'posts': queryset })
    else:
        return render(request, 'search.html', { 'query_string': 'Null', 'found_entries': 'Enter a search term' })
        