# flaskResumeAPI
Serves up my resume as a Flask-powered API using mod_wsgi and Apache

##API Reference

###API Root
Endpoint | Methods | Function
--- | --- | ---
/ | GET | Access API root index 

###Contact Info
Endpoint | Methods | Function
--- | --- | ---
/contact/ | GET, POST | Access resume contact info

###Education Info
Endpoint | Methods | Function
--- | --- | ---
/education/ | GET, POST | Access all education info  
/education/<int:id> | GET | Access single degree detail 

###Career Info
Endpoint | Methods | Function
--- | --- | ---
/career/ | GET, POST | Access all career info     
/career/<int:id> | GET | Access single job detail    

###Projects Info
Endpoint | Methods | Function
--- | --- | ---
/projects/ | GET, POST | Access all projects info   
/project/<int:id> | GET | Access single project detail 

###Skills Info
Endpoint | Methods | Function
--- | --- | ---
/skills/ | GET, POST | Access all skills info    
/skill/<int:id> | GET | Access single skill detail  
