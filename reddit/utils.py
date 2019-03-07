#Save data as json 
def save_as_json(df,name):
    path_ = 'result/'+name+'.json'
    df.to_json(path_)