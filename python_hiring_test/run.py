import pandas as pd 
import datetime

#BA – Batting average (also abbreviated AVG): hits divided by at bats (H/AB)    
def batting_avg(df):
    return (df['H'] / df['AB'])
    
#OBP – On-base percentage: times reached base (H + BB + HBP) divided by 
#at bats plus walks plus hit by pitch plus sacrifice flies (AB + BB + HBP + SF)
def onbase_percentage(df):
    return ((df['H'] + df['BB'] + df['HBP']) / (df['AB'] + df['BB'] + df['HBP'] + df['SF']))

#SLG – Slugging average: total bases achieved on hits divided by at-bats (TB/AB)
def sluggin_avg(df):
    return (df['TB'] / df['AB'])

#OPS – On-base plus slugging: on-base percentage plus slugging average
def onbase_plus_slug(df):
    return (onbase_percentage(df) + sluggin_avg(df))

#selecting dataframe with only TRUE condition met in condition
vs_Map = {'vs RHP': lambda df : df[df['PitcherSide'] == 'R'],
        'vs LHP': lambda df : df[df['PitcherSide'] == 'L'],
        'vs RHH': lambda df : df[df['HitterSide'] == 'R'],
        'vs LHH': lambda df : df[df['HitterSide'] == 'L'] }

def sum_stats(pitch_data, combination):
    
    #spliting the combination
    s = combination.strip().split(',')
    
    #performing split apply combine
    g = vs_Map[s[2]](pitch_data).groupby(s[1])
    sum_of_stats = g[['PA', 'AB', 'H','2B', '3B', 'HR', 'TB', 'BB', 'SF', 'HBP']].sum()
    #doing sum of selective columns improves performance -- Execution Time datetime.timedelta(0, 0, 619460)
    #without column specifiacation -- Exec Time datetime.timedelta(0, 0, 663477)
    
    #Including subjects with PA >= 25
    filtered_df = sum_of_stats[sum_of_stats.PA >=25]
    
    #based on combination input calculating Values
    
    if s[0] == 'AVG':
        value = pd.Series(batting_avg(filtered_df))
    elif s[0] == 'OBP':
        value = pd.Series(onbase_percentage(filtered_df))
    elif s[0] == 'SLG':
        value = pd.Series(sluggin_avg(filtered_df))
    else:
        value = pd.Series(onbase_plus_slug(filtered_df))

    # create dataframe by adding value and return
    ouput_df = pd.DataFrame({'SubjectId' : filtered_df.index, 'Stat' : s[0],
                             'Subject' : s[1], 'Split' : s[2],
                             'Value' : value.round(3)},
                            columns=['SubjectId','Stat', 'Split', 'Subject', 'Value'])
    ouput_df = ouput_df.reset_index(drop = True)
    return ouput_df[['SubjectId', 'Stat', 'Split', 'Subject', 'Value']]




def main():
    input_data = pd.read_csv('./data/raw/pitchdata.csv')
    combinations = open('./data/reference/combinations.txt').readlines()[1:]
    
    # create output dataframe with Column names
    output = pd.DataFrame(columns=['SubjectId', 'Stat', 'Split', 'Subject', 'Value'])
    
    #iterating through statistic combinations to process
    for line in combinations:
        calc_stat = sum_stats(pitch_data, line)
        output = output.append(calc_stat)
    output = output.sort_values(by = ['SubjectId', 'Stat', 'Split', 'Subject']) 
    output[['SubjectId', 'Stat', 'Split', 'Subject', 'Value']].to_csv('data/processed/output.csv',index = False)

    
if __name__ == '__main__':
    main()
    