# jobplus18-1
《楼+ Python 实战》第 18 期第 1 组

# Contributors
*[纠结中的忐忑](https://github.com/xglvdai/)


# Step
`git clone https://github.com/xglvdai/jobplus18-1`

`sudo pip3 install -r requirements.txt`

`sudo servcie mysql start`

`mysql -uroot -e 'create schema jobplus charset = utf8' `

`cd jobplus18-1`

`export FLASK_APP=manage.py`

`flask db migrate`

`flask db upgrade`

`FLASK_DEBUG=1 FLASK_APP=manage.py flask run`

