from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

#매트릭스랑 평점 같은 영화제목 가져오기
movie = db.movies.find_one({'title':'매트릭스'})

target_star = movie['star']
target_movies= list(db.movies.find({'star':target_star},{'_id':False}))
for target in target_movies:
    print(target['title'])

#특정영화 평점바꾸기
# db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})