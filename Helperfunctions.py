import pandas as pd
from IPython.display import display,clear_output, Image, HTML
import pycountry_convert
import pycountry
import pycountry_convert

def generate_html_table(age,league,club,comp_data,best_position,nationality,market_value,all_achievements,club_apps_int_cups,club_goals_int_cups,club_assists_int_cups,club_mins_int_cups,
                        club_goals,national_goals,club_apps,national_apps,club_mins,national_mins,club_assists,
                        national_assists,pred_overall,pred_potential):
    # Create the HTML table structure
    html = f"""
        <table style="margin-left:auto; margin-right:auto;">
        <tr>
            <td><strong>Age:</strong></td>
            <td>{age}</td>
        </tr>
        <tr>
            <td><strong>League:</strong></td>
            <td>{league}</td>
        </tr>
        <tr>
            <td><strong>Club:</strong></td>
            <td>{club}</td>
        </tr>
        <tr>
            <td><strong>Position:</strong></td>
            <td>{best_position}</td>
        </tr>
        <tr>
            <td><strong>Nationality:</strong></td>
            <td>{nationality}</td>
        </tr>
        <tr>
            <td><strong>Market Value:</strong></td>
            <td>€{market_value}</td>
        </tr>
        <tr>
            <td><strong>Total Achievements:</strong></td>
            <td>{all_achievements}</td>
        </tr>
        </table>
        """

    html+= "<br>\n"


    html += '<table style="margin-left:auto; margin-right:auto;">\n'

    html += "<tr><th></th>"
    categories = ['Games', 'Goals', 'Assists', 'Minutes']
    for category in categories:
        html += "<th>{}</th>".format(category)
    html += "</tr>\n"

    competitions = {
        'Clubs': {
            'apps': club_apps,
            'goals': club_goals,
            'assists': club_assists,
            'minutes': club_mins
        },
        'National Team': {
            'apps': national_apps,
            'goals': national_goals,
            'assists': national_assists,
            'minutes': national_mins
        },
        'Total': {
            'apps': club_apps + national_apps ,
            'goals': club_goals + national_goals ,
            'assists': club_assists + national_assists,
            'minutes': club_mins + national_mins
        }

    }

    for competition, data in competitions.items():
        if data['apps'] > 0:
            html += "<tr><th>{}</th>".format(competition)
            html += "<td>{}</td><td>{}</td><td>{}</td><td>{}</td>".format(
                data['apps'], data['goals'], data['assists'], data['minutes'])
            html += "</tr>\n"

    html += "</table>"

    html += "<br>\n"

    html += "<br>\n"

    html += '<table style="margin-left:auto; margin-right:auto;">\n'

    html += "<tr><th></th>"
    categories = ['Games', 'Goals', 'Assists', 'Minutes']
    for category in categories:
        html += "<th>{}</th>".format(category)
    html += "</tr>\n"

    competitions = {
        
        'UEFA Champions League': {
            'apps': comp_data['Champions League Qu._apps'] + comp_data['Champions League_apps'],
            'goals': comp_data['Champions League Qu._goals'] + comp_data['Champions League_goals'],
            'assists': comp_data['Champions League Qu._assists'] + comp_data['Champions League_assists'],
            'minutes': comp_data['Champions League Qu._mins'] + comp_data['Champions League_mins']
        },
        'Europa League': {
            'apps': comp_data['Europa League_apps'] + comp_data['Europa League Qualifying_apps'],
            'goals': comp_data['Europa League_goals'] + comp_data['Europa League Qualifying_goals'],
            'assists': comp_data['Europa League_assists'] + comp_data['Europa League Qualifying_assists'],
            'minutes': comp_data['Europa League_mins'] + comp_data['Europa League Qualifying_mins']
        },
        'Conference League': {
            'apps': comp_data['Conference League_apps']+comp_data['UECL Qualifiers_apps'],
            'goals': comp_data['Conference League_goals']+comp_data['UECL Qualifiers_goals'],
            'assists': comp_data['Conference League_assists']+comp_data['UECL Qualifiers_assists'],
            'minutes': comp_data['Conference League_mins']+comp_data['UECL Qualifiers_mins']
        },
        'Libertadores': {
            'apps': comp_data['Libertadores_apps'],
            'goals': comp_data['Libertadores_goals'],
            'assists': comp_data['Libertadores_assists'],
            'minutes': comp_data['Libertadores_mins']
        },
        'Sudamericana': {
            'apps': comp_data['Copa Sudamericana_apps'],
            'goals': comp_data['Copa Sudamericana_goals'],
            'assists': comp_data['Copa Sudamericana_assists'],
            'minutes': comp_data['Copa Sudamericana_mins']
        },
        'CONCACAF Champions League': {
            'apps': comp_data['CONCACAF Champions League_apps'],
            'goals': comp_data['CONCACAF Champions League_goals'],
            'assists': comp_data['CONCACAF Champions League_assists'],
            'minutes': comp_data['CONCACAF Champions League_mins']
        },
        'CAF Champions League': {
            'apps': comp_data['CAF-Champions League_apps'],
            'goals': comp_data['CAF-Champions League_goals'],
            'assists': comp_data['CAF-Champions League_assists'],
            'minutes': comp_data['CAF-Champions League_mins']
        },        
        'AFC Champions League': {
            'apps': comp_data['AFC Champions League_apps'],
            'goals': comp_data['AFC Champions League_goals'],
            'assists': comp_data['AFC Champions League_assists'],
            'minutes': comp_data['AFC Champions League_mins']
        },        
        'UEFA Youth Champions League': {
            'apps': comp_data['UEFA Youth League_apps'],
            'goals': comp_data['UEFA Youth League_goals'],
            'assists': comp_data['UEFA Youth League_assists'],
            'minutes': comp_data['UEFA Youth League_mins']
        },
        'Other International Cups':{
            'apps':club_apps_int_cups - (comp_data['UEFA Youth League_apps']+comp_data['AFC Champions League_apps']+
                                         comp_data['CAF-Champions League_apps']+comp_data['CONCACAF Champions League_apps']+
                                         comp_data['Copa Sudamericana_apps']+comp_data['Libertadores_apps']+comp_data['Conference League_apps']+
                                         comp_data['UECL Qualifiers_apps']+comp_data['Europa League_apps']+ comp_data['Europa League Qualifying_apps']+
                                         comp_data['Champions League Qu._apps'] + comp_data['Champions League_apps']),
            'goals':club_goals_int_cups - (comp_data['UEFA Youth League_goals']+comp_data['AFC Champions League_goals']+
                                         comp_data['CAF-Champions League_goals']+comp_data['CONCACAF Champions League_goals']+
                                         comp_data['Copa Sudamericana_goals']+comp_data['Libertadores_goals']+comp_data['Conference League_goals']+
                                         comp_data['UECL Qualifiers_goals']+comp_data['Europa League_goals']+ comp_data['Europa League Qualifying_goals']+
                                         comp_data['Champions League Qu._goals'] + comp_data['Champions League_goals']),
            'assists':club_assists_int_cups - (comp_data['UEFA Youth League_assists']+comp_data['AFC Champions League_assists']+
                                         comp_data['CAF-Champions League_assists']+comp_data['CONCACAF Champions League_assists']+
                                         comp_data['Copa Sudamericana_assists']+comp_data['Libertadores_assists']+comp_data['Conference League_assists']+
                                         comp_data['UECL Qualifiers_assists']+comp_data['Europa League_assists']+ comp_data['Europa League Qualifying_assists']+
                                         comp_data['Champions League Qu._assists'] + comp_data['Champions League_assists']),
            'minutes':club_mins_int_cups - (comp_data['UEFA Youth League_mins']+comp_data['AFC Champions League_mins']+
                                         comp_data['CAF-Champions League_mins']+comp_data['CONCACAF Champions League_mins']+
                                         comp_data['Copa Sudamericana_mins']+comp_data['Libertadores_mins']+comp_data['Conference League_mins']+
                                         comp_data['UECL Qualifiers_mins']+comp_data['Europa League_mins']+ comp_data['Europa League Qualifying_mins']+
                                         comp_data['Champions League Qu._mins'] + comp_data['Champions League_mins']),
        },
        'Total':{
            'apps':club_apps_int_cups,
            'goals':club_goals_int_cups,
            'assists':club_assists_int_cups,
            'minutes':club_mins_int_cups
        }

    }

    for competition, data in competitions.items():
        if data['apps'] > 0:
            html += "<tr><th>{}</th>".format(competition)
            html += "<td>{}</td><td>{}</td><td>{}</td><td>{}</td>".format(
                data['apps'], data['goals'], data['assists'], data['minutes'])
            html += "</tr>\n"

    html += "</table>"

    html += "<br>\n"

    html += f"""
        <table style="margin-left:auto; margin-right:auto;">
        <tr>
            <td><strong>Predicted overall rating:</strong></td>
            <td>{pred_overall[0]}</td>
        </tr>
        <tr>
            <td><strong>Predicted potential rating:</strong></td>
            <td>{pred_potential[0]}</td>
        </tr>
        </table>
        """
    return html

def clean_df():
    df = pd.read_excel('Final Players 06062023.xlsx')
    df[["market_value"]] = df[["market_value"]].astype("float64")
    df = df.dropna(subset=['besoccer_player_Ranking'])
    #Selecting only rows that are up to date with the game version 230033 (June 10, 2023)
    df = df[df['fifa_last_update'] == 230038]

    cols_to_drop = ['sofifa_id', 'name', 'besoccer_link', 'birthday', 'transfermarkt_link', 
                    'weak_foot', 'skill_moves', 'international_repuation', 'sofifa_markt_value',
                    'sofifa_wage', 'sofifa_release_clause', 'pace', 'shooting', 'passing',
                    'dribbling_overall', 'defense', 'physical', 'sofifa_link', 'crossing',
                    'finishing', 'heading_accuracy', 'short_passing', 'volleys', 'dribbling',
                    'curve', 'fk_accuracy', 'long_passing', 'ball_control', 'acceleration',
                    'sprint_speed', 'agility', 'reactions', 'balance', 'shot_power', 'jumping',
                    'stamina', 'strength', 'long_shots', 'aggression', 'interceptions', 'positioning',
                    'vision', 'penalties', 'composure', 'defensive_awareness', 'standing_tackle',
                    'sliding_tackle', 'gk_diving', 'gk_handling', 'gk_kicking', 'gk_positioning',
                    'gk_reflexes', 'fifa_last_update','LS','ST','RS','LW','LF','CF','RF','RW','LAM',
                    'CAM','RAM','LM','LCM','CM','RCM','RM','LWB','LDM','CDM','RDM','RWB','LB','LCB','CB','RCB','RB','GK']

    df = df.drop(columns=cols_to_drop)
    unique_leagues = df.loc[df['club_name'] == 'CD Universidad Católica', 'league_name'].unique()
    league_counts = pd.Series(unique_leagues).value_counts()
    df.loc[(df['club_name'] == 'CD Universidad Católica') & (df['league_name'] == '[Ecuador 1st Tier] Serie A Primera Etapa'), 'club_name'] += ' Ecuador'
    df.loc[(df['club_name'] == 'CD Universidad Católica') & (df['league_name'] == '[Chile 1st Tier] Primera División'), 'club_name'] += ' Chile'


    # create mapping dictionary for nationalities and continents
    continent_dict = {}
    for country in pycountry.countries:
        alpha2_code = country.alpha_2
        try:
            continent_code = pycountry_convert.convert_continent_code_to_continent_name(pycountry_convert.country_alpha2_to_continent_code(alpha2_code))
            continent_dict[country.name] = continent_code
        except KeyError:
            continue


    # assuming your dataframe is named 'my_dataset'
    nationality_column = df['nationality']
    continent_column = nationality_column.map(continent_dict)

    # add the new continent column to the dataframe
    df['continent'] = continent_column
    # get unique nationalities from the dataset
    dataset_nationalities = set(df['nationality'].unique())

    # get unique nationalities from the mapping dictionary
    mapped_nationalities = set(continent_dict.keys())

    # find the nationalities that weren't mapped
    unmapped_nationalities = dataset_nationalities - mapped_nationalities
    continent_dict = {}
    for country in pycountry.countries:
        alpha2_code = country.alpha_2
        try:
            continent_code = pycountry_convert.convert_continent_code_to_continent_name(pycountry_convert.country_alpha2_to_continent_code(alpha2_code))
            continent_dict[country.name] = continent_code
        except KeyError:
            continue
        
    continent_dict['Vietnam'] = 'Asia'
    continent_dict['Kosovo'] = 'Europe'
    continent_dict['Tanzania'] = 'Africa'
    continent_dict['China PR'] = 'Asia'
    continent_dict['Moldova'] = 'Europe'
    continent_dict['Cape Verde Islands'] = 'Africa'
    continent_dict['England'] = 'Europe'
    continent_dict['Congo DR'] = 'Africa'
    continent_dict['Palestine'] = 'Asia'
    continent_dict['Chinese Taipei'] = 'Asia'
    continent_dict['Syria'] = 'Asia'
    continent_dict['Curacao'] = 'North America'
    continent_dict['Guinea Bissau'] = 'Africa'
    continent_dict['São Tomé e Príncipe'] = 'Africa'
    continent_dict['Scotland'] = 'Europe'
    continent_dict['Wales'] = 'Europe'
    continent_dict['Korea Republic'] = 'Asia'
    continent_dict['Northern Ireland'] = 'Europe'
    continent_dict['Bolivia'] = 'South America'
    continent_dict['Czech Republic'] = 'Europe'
    continent_dict['Iran'] = 'Asia'
    continent_dict['Venezuela'] = 'South America'
    continent_dict['Korea DPR'] = 'Asia'
    continent_dict['Russia'] = 'Europe'
    continent_dict['Republic of Ireland'] = 'Europe'
    continent_dict['Korea, South'] = 'Asia'
    continent_dict['Cape Verde']='Africa'
    continent_dict['DR Congo'] = 'Africa'
    continent_dict['Bosnia-Herzegovina'] = 'Europe'
    continent_dict["Cote d'Ivoire"] = 'Africa'
    

    nationality_column = df['nationality']
    continent_column = nationality_column.map(continent_dict)

    # add the new continent column to the dataframe
    df['continent'] = continent_column
    nationality_column = df['nationality']
    continent_column = nationality_column.map(continent_dict)

    # add the new continent column to the dataframe
    df['continent'] = continent_column
    # Assuming your clean_data dataframe is already loaded

    # Create an empty dictionary to hold the results
    leagues_dict = {}

    # Loop through unique values in league_name column
    for league in df['league_name'].unique():
        # Create a subset of the dataframe for this league
        league_subset = df[df['league_name'] == league]
        
        # Get unique club_names for this league
        clubs_name = league_subset['club_name'].unique()
        
        # Add the league and its corresponding clubs to the dictionary
        leagues_dict[league] = clubs_name

    countries_dict ={}

    for continents in df['continent'].unique():
        
        continent_subset = df[df['continent'] == continents]
        
        countries = continent_subset['nationality'].unique()
        
        countries_dict[continents] = countries
    cat_vars = ['league_name', 'best_position', 'continent','nationality']



    num_vars = ["bessocer_elo","besoccer_player_Ranking",'age','Club Ranking footysimulator','market_value','Club appearances','Club Goals',
            'Club Assists','Club Minutes','National appearances','National Goals','National Assists','National Minutes',
            "achievemnts_count","First Tier appearances","First Tier Goals","First Tier Assists","First Tier Minutes","Last season appearances",
            "Last season Goals","Last season Assists","Last season Minutes","int_cups_appearances","int_cups_goals","int_cups_assists","int_cups_minutes","CAF-Champions League_apps","CAF-Champions League_goals","CAF-Champions League_assists",
            "CAF-Champions League_mins","CONCACAF Champions League_apps","CONCACAF Champions League_goals","CONCACAF Champions League_assists","CONCACAF Champions League_mins",
            "Libertadores_apps","Libertadores_goals","Libertadores_assists","Libertadores_mins","Copa Sudamericana_apps","Copa Sudamericana_goals","Copa Sudamericana_assists",
            "Copa Sudamericana_mins","Champions League Qu._apps","Champions League Qu._goals","Champions League Qu._assists","Champions League Qu._mins","Champions League_apps",
            "Champions League_goals","Champions League_assists","Champions League_mins","Europa League_apps","Europa League_goals","Europa League_assists","Europa League_mins",
            "Europa League Qualifying_apps","Europa League Qualifying_goals","Europa League Qualifying_assists","Europa League Qualifying_mins","Conference League_apps","Conference League_goals",
            "Conference League_assists","Conference League_mins","UECL Qualifiers_apps","UECL Qualifiers_goals","UECL Qualifiers_assists","UECL Qualifiers_mins","UEFA Youth League_apps",
            "UEFA Youth League_goals","UEFA Youth League_assists","UEFA Youth League_mins","AFC Champions League_apps","AFC Champions League_goals","AFC Champions League_assists",
            "AFC Champions League_mins"]

    df[cat_vars]=df[cat_vars].astype('category')
    # Encode categorical variables

    clean_data = pd.get_dummies(df.drop(['club_name'],axis=1), columns=cat_vars)
    
    return clean_data,leagues_dict,countries_dict,num_vars


def clean_data_players(brasilerao):


    continent_dict = {}
    for country in pycountry.countries:
        alpha2_code = country.alpha_2
        try:
            continent_code = pycountry_convert.convert_continent_code_to_continent_name(pycountry_convert.country_alpha2_to_continent_code(alpha2_code))
            continent_dict[country.name] = continent_code
        except KeyError:
            continue


    # assuming your dataframe is named 'my_dataset'
    nationality_column = brasilerao['nationality']
    continent_column = nationality_column.map(continent_dict)

    # add the new continent column to the dataframe
    brasilerao['continent'] = continent_column
    # get unique nationalities from the dataset
    dataset_nationalities = set(brasilerao['nationality'].unique())

    # get unique nationalities from the mapping dictionary
    mapped_nationalities = set(continent_dict.keys())

    # find the nationalities that weren't mapped
    unmapped_nationalities = dataset_nationalities - mapped_nationalities
    continent_dict = {}
    for country in pycountry.countries:
        alpha2_code = country.alpha_2
        try:
            continent_code = pycountry_convert.convert_continent_code_to_continent_name(pycountry_convert.country_alpha2_to_continent_code(alpha2_code))
            continent_dict[country.name] = continent_code
        except KeyError:
            continue
        
    continent_dict['Vietnam'] = 'Asia'
    continent_dict['Kosovo'] = 'Europe'
    continent_dict['Tanzania'] = 'Africa'
    continent_dict['China PR'] = 'Asia'
    continent_dict['Moldova'] = 'Europe'
    continent_dict['Cape Verde Islands'] = 'Africa'
    continent_dict['England'] = 'Europe'
    continent_dict['Congo DR'] = 'Africa'
    continent_dict['Palestine'] = 'Asia'
    continent_dict['Chinese Taipei'] = 'Asia'
    continent_dict['Syria'] = 'Asia'
    continent_dict['Curacao'] = 'North America'
    continent_dict['Guinea Bissau'] = 'Africa'
    continent_dict['São Tomé e Príncipe'] = 'Africa'
    continent_dict['Scotland'] = 'Europe'
    continent_dict['Wales'] = 'Europe'
    continent_dict['Korea Republic'] = 'Asia'
    continent_dict['Northern Ireland'] = 'Europe'
    continent_dict['Bolivia'] = 'South America'
    continent_dict['Czech Republic'] = 'Europe'
    continent_dict['Iran'] = 'Asia'
    continent_dict['Venezuela'] = 'South America'
    continent_dict['Korea DPR'] = 'Asia'
    continent_dict['Russia'] = 'Europe'
    continent_dict['Republic of Ireland'] = 'Europe'
    continent_dict['Korea, South'] = 'Asia'
    continent_dict['Cape Verde']='Africa'
    continent_dict['DR Congo'] = 'Africa'
    continent_dict['Bosnia-Herzegovina'] = 'Europe'
    continent_dict["Cote d'Ivoire"] = 'Africa'



    nationality_column = brasilerao['nationality']
    continent_column = nationality_column.map(continent_dict)

    # add the new continent column to the dataframe
    brasilerao['continent'] = continent_column
    nationality_column = brasilerao['nationality']
    continent_column = nationality_column.map(continent_dict)

    # add the new continent column to the dataframe
    brasilerao['continent'] = continent_column

    cat_vars = ['league_name', 'best_position', 'continent','nationality']
    num_vars1 = ["bessocer_elo","besoccer_player_Ranking",'age','Club Ranking footysimulator','market_value','Club appearances','Club Goals',
            'Club Assists','Club Minutes','National appearances','National Goals','National Assists','National Minutes',
            "achievemnts_count","First Tier appearances","First Tier Goals","First Tier Assists","First Tier Minutes","Last season appearances",
            "Last season Goals","Last season Assists","Last season Minutes","int_cups_appearances","int_cups_goals","int_cups_assists","int_cups_minutes","CAF-Champions League_apps","CAF-Champions League_goals","CAF-Champions League_assists",
            "CAF-Champions League_mins","CONCACAF Champions League_apps","CONCACAF Champions League_goals","CONCACAF Champions League_assists","CONCACAF Champions League_mins",
            "Libertadores_apps","Libertadores_goals","Libertadores_assists","Libertadores_mins","Copa Sudamericana_apps","Copa Sudamericana_goals","Copa Sudamericana_assists",
            "Copa Sudamericana_mins","Champions League Qu._apps","Champions League Qu._goals","Champions League Qu._assists","Champions League Qu._mins","Champions League_apps",
            "Champions League_goals","Champions League_assists","Champions League_mins","Europa League_apps","Europa League_goals","Europa League_assists","Europa League_mins",
            "Europa League Qualifying_apps","Europa League Qualifying_goals","Europa League Qualifying_assists","Europa League Qualifying_mins","Conference League_apps","Conference League_goals",
            "Conference League_assists","Conference League_mins","UECL Qualifiers_apps","UECL Qualifiers_goals","UECL Qualifiers_assists","UECL Qualifiers_mins","UEFA Youth League_apps",
            "UEFA Youth League_goals","UEFA Youth League_assists","UEFA Youth League_mins","AFC Champions League_apps","AFC Champions League_goals","AFC Champions League_assists",
            "AFC Champions League_mins"]
    
    brasilerao[cat_vars]=brasilerao[cat_vars].astype('category')
    brasilerao_encoded = pd.get_dummies(brasilerao.drop(['club_name','name'], axis=1))

    return brasilerao_encoded,num_vars1



def no_league_clean_data_players(brasilerao):


    continent_dict = {}
    for country in pycountry.countries:
        alpha2_code = country.alpha_2
        try:
            continent_code = pycountry_convert.convert_continent_code_to_continent_name(pycountry_convert.country_alpha2_to_continent_code(alpha2_code))
            continent_dict[country.name] = continent_code
        except KeyError:
            continue


    # assuming your dataframe is named 'my_dataset'
    nationality_column = brasilerao['nationality']
    continent_column = nationality_column.map(continent_dict)

    # add the new continent column to the dataframe
    brasilerao['continent'] = continent_column
    # get unique nationalities from the dataset
    dataset_nationalities = set(brasilerao['nationality'].unique())

    # get unique nationalities from the mapping dictionary
    mapped_nationalities = set(continent_dict.keys())

    # find the nationalities that weren't mapped
    unmapped_nationalities = dataset_nationalities - mapped_nationalities
    continent_dict = {}
    for country in pycountry.countries:
        alpha2_code = country.alpha_2
        try:
            continent_code = pycountry_convert.convert_continent_code_to_continent_name(pycountry_convert.country_alpha2_to_continent_code(alpha2_code))
            continent_dict[country.name] = continent_code
        except KeyError:
            continue
        
    continent_dict['Vietnam'] = 'Asia'
    continent_dict['Kosovo'] = 'Europe'
    continent_dict['Tanzania'] = 'Africa'
    continent_dict['China PR'] = 'Asia'
    continent_dict['Moldova'] = 'Europe'
    continent_dict['Cape Verde Islands'] = 'Africa'
    continent_dict['England'] = 'Europe'
    continent_dict['Congo DR'] = 'Africa'
    continent_dict['Palestine'] = 'Asia'
    continent_dict['Chinese Taipei'] = 'Asia'
    continent_dict['Syria'] = 'Asia'
    continent_dict['Curacao'] = 'North America'
    continent_dict['Guinea Bissau'] = 'Africa'
    continent_dict['São Tomé e Príncipe'] = 'Africa'
    continent_dict['Scotland'] = 'Europe'
    continent_dict['Wales'] = 'Europe'
    continent_dict['Korea Republic'] = 'Asia'
    continent_dict['Northern Ireland'] = 'Europe'
    continent_dict['Bolivia'] = 'South America'
    continent_dict['Czech Republic'] = 'Europe'
    continent_dict['Iran'] = 'Asia'
    continent_dict['Venezuela'] = 'South America'
    continent_dict['Korea DPR'] = 'Asia'
    continent_dict['Russia'] = 'Europe'
    continent_dict['Republic of Ireland'] = 'Europe'
    continent_dict['Korea, South'] = 'Asia'
    continent_dict['Cape Verde']='Africa'
    continent_dict['DR Congo'] = 'Africa'
    continent_dict['Bosnia-Herzegovina'] = 'Europe'
    continent_dict["Cote d'Ivoire"] = 'Africa'



    nationality_column = brasilerao['nationality']
    continent_column = nationality_column.map(continent_dict)

    # add the new continent column to the dataframe
    brasilerao['continent'] = continent_column
    nationality_column = brasilerao['nationality']
    continent_column = nationality_column.map(continent_dict)

    # add the new continent column to the dataframe
    brasilerao['continent'] = continent_column

    cat_vars = ['best_position', 'continent','nationality']
    num_vars1 = ["bessocer_elo","besoccer_player_Ranking",'age','Club Ranking footysimulator','market_value','Club appearances','Club Goals',
            'Club Assists','Club Minutes','National appearances','National Goals','National Assists','National Minutes',
            "achievemnts_count","First Tier appearances","First Tier Goals","First Tier Assists","First Tier Minutes","Last season appearances",
            "Last season Goals","Last season Assists","Last season Minutes","int_cups_appearances","int_cups_goals","int_cups_assists","int_cups_minutes","CAF-Champions League_apps","CAF-Champions League_goals","CAF-Champions League_assists",
            "CAF-Champions League_mins","CONCACAF Champions League_apps","CONCACAF Champions League_goals","CONCACAF Champions League_assists","CONCACAF Champions League_mins",
            "Libertadores_apps","Libertadores_goals","Libertadores_assists","Libertadores_mins","Copa Sudamericana_apps","Copa Sudamericana_goals","Copa Sudamericana_assists",
            "Copa Sudamericana_mins","Champions League Qu._apps","Champions League Qu._goals","Champions League Qu._assists","Champions League Qu._mins","Champions League_apps",
            "Champions League_goals","Champions League_assists","Champions League_mins","Europa League_apps","Europa League_goals","Europa League_assists","Europa League_mins",
            "Europa League Qualifying_apps","Europa League Qualifying_goals","Europa League Qualifying_assists","Europa League Qualifying_mins","Conference League_apps","Conference League_goals",
            "Conference League_assists","Conference League_mins","UECL Qualifiers_apps","UECL Qualifiers_goals","UECL Qualifiers_assists","UECL Qualifiers_mins","UEFA Youth League_apps",
            "UEFA Youth League_goals","UEFA Youth League_assists","UEFA Youth League_mins","AFC Champions League_apps","AFC Champions League_goals","AFC Champions League_assists",
            "AFC Champions League_mins"]
    
    brasilerao[cat_vars]=brasilerao[cat_vars].astype('category')
    brasilerao_encoded = pd.get_dummies(brasilerao.drop(['club_name','name','league_name'], axis=1))

    return brasilerao_encoded,num_vars1

def clean_df_11pick():

    df = pd.read_excel('Final Players 06062023.xlsx')
    df[["market_value"]] = df[["market_value"]].astype("float64")
    df = df.dropna(subset=['besoccer_player_Ranking'])
    # #Selecting only rows that are up to date with the game version 230033 (June 10, 2023)
    df = df[df['fifa_last_update'] == 230038]
    df['club_name'] = df['club_name'].replace('FK Bodø/Glimt', 'FK Bodø Glimt')

    cols_to_drop = ['besoccer_link', 'birthday', 'weak_foot', 'skill_moves', 'international_repuation', 'sofifa_markt_value',
                    'sofifa_wage', 'sofifa_release_clause','crossing',
                    'finishing', 'heading_accuracy', 'short_passing', 'volleys', 'dribbling',
                    'curve', 'fk_accuracy', 'long_passing', 'ball_control', 'acceleration',
                    'sprint_speed', 'agility', 'reactions', 'balance', 'shot_power', 'jumping',
                    'stamina', 'strength', 'long_shots', 'aggression', 'interceptions', 'positioning',
                    'vision', 'penalties', 'composure', 'defensive_awareness', 'standing_tackle',
                    'sliding_tackle', 'gk_diving', 'gk_handling', 'gk_kicking', 'gk_positioning',
                    'gk_reflexes', 'fifa_last_update',]

    df = df.drop(columns=cols_to_drop)
    unique_leagues = df.loc[df['club_name'] == 'CD Universidad Católica', 'league_name'].unique()
    league_counts = pd.Series(unique_leagues).value_counts()
    df.loc[(df['club_name'] == 'CD Universidad Católica') & (df['league_name'] == '[Ecuador 1st Tier] Serie A Primera Etapa'), 'club_name'] += ' Ecuador'
    df.loc[(df['club_name'] == 'CD Universidad Católica') & (df['league_name'] == '[Chile 1st Tier] Primera División'), 'club_name'] += ' Chile'


    # create mapping dictionary for nationalities and continents
    continent_dict = {}
    for country in pycountry.countries:
        alpha2_code = country.alpha_2
        try:
            continent_code = pycountry_convert.convert_continent_code_to_continent_name(pycountry_convert.country_alpha2_to_continent_code(alpha2_code))
            continent_dict[country.name] = continent_code
        except KeyError:
            continue


    # assuming your dataframe is named 'my_dataset'
    nationality_column = df['nationality']
    continent_column = nationality_column.map(continent_dict)

    # add the new continent column to the dataframe
    df['continent'] = continent_column
    # get unique nationalities from the dataset
    dataset_nationalities = set(df['nationality'].unique())

    # get unique nationalities from the mapping dictionary
    mapped_nationalities = set(continent_dict.keys())

    # find the nationalities that weren't mapped
    unmapped_nationalities = dataset_nationalities - mapped_nationalities
    continent_dict = {}
    for country in pycountry.countries:
        alpha2_code = country.alpha_2
        try:
            continent_code = pycountry_convert.convert_continent_code_to_continent_name(pycountry_convert.country_alpha2_to_continent_code(alpha2_code))
            continent_dict[country.name] = continent_code
        except KeyError:
            continue
        
    continent_dict['Vietnam'] = 'Asia'
    continent_dict['Kosovo'] = 'Europe'
    continent_dict['Tanzania'] = 'Africa'
    continent_dict['China PR'] = 'Asia'
    continent_dict['Moldova'] = 'Europe'
    continent_dict['Cape Verde Islands'] = 'Africa'
    continent_dict['England'] = 'Europe'
    continent_dict['Congo DR'] = 'Africa'
    continent_dict['Palestine'] = 'Asia'
    continent_dict['Chinese Taipei'] = 'Asia'
    continent_dict['Syria'] = 'Asia'
    continent_dict['Curacao'] = 'North America'
    continent_dict['Guinea Bissau'] = 'Africa'
    continent_dict['São Tomé e Príncipe'] = 'Africa'
    continent_dict['Scotland'] = 'Europe'
    continent_dict['Wales'] = 'Europe'
    continent_dict['Korea Republic'] = 'Asia'
    continent_dict['Northern Ireland'] = 'Europe'
    continent_dict['Bolivia'] = 'South America'
    continent_dict['Czech Republic'] = 'Europe'
    continent_dict['Iran'] = 'Asia'
    continent_dict['Venezuela'] = 'South America'
    continent_dict['Korea DPR'] = 'Asia'
    continent_dict['Russia'] = 'Europe'
    continent_dict['Republic of Ireland'] = 'Europe'
    continent_dict['Korea, South'] = 'Asia'
    continent_dict['Cape Verde']='Africa'
    continent_dict['DR Congo'] = 'Africa'
    continent_dict['Bosnia-Herzegovina'] = 'Europe'
    continent_dict["Cote d'Ivoire"] = 'Africa'
    

    nationality_column = df['nationality']
    continent_column = nationality_column.map(continent_dict)

    # add the new continent column to the dataframe
    df['continent'] = continent_column
    nationality_column = df['nationality']
    continent_column = nationality_column.map(continent_dict)

    # add the new continent column to the dataframe
    df['continent'] = continent_column
    # Assuming your clean_data dataframe is already loaded

    # Create an empty dictionary to hold the results
    leagues_dict = {}

    # Loop through unique values in league_name column
    for league in df['league_name'].unique():
        # Create a subset of the dataframe for this league
        league_subset = df[df['league_name'] == league]
        
        # Get unique club_names for this league
        clubs_name = league_subset['club_name'].unique()
        
        # Add the league and its corresponding clubs to the dictionary
        leagues_dict[league] = clubs_name

    countries_dict ={}

    for continents in df['continent'].unique():
        
        continent_subset = df[df['continent'] == continents]
        
        countries = continent_subset['nationality'].unique()
        
        countries_dict[continents] = countries
    return df