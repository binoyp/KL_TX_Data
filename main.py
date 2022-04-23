from kl_tx_data import set_gov_body, Session, engine, Base, LocalBody

Base.metadata.create_all(engine)

sess = Session()


for i in range(160,1500 ):

    res, data = set_gov_body(i)

    if res:
        name , type_info = data 

        lbd = LocalBody(id=i,name= name, loc_type= type_info )

        sess.add(lbd)
        sess.commit()
    

        print(name,data  )

sess.close()