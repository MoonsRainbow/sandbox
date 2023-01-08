# sandbox

### #1. sandbox 소개. 
Introducing the sandbox module.  
<br><br>

- 이 모듈은 소프트웨어 개발을 진행할 때 개인적으로 가장 많이 작성한 코드들을 모아두었습니다.  
This module is a compilation of the most personally written codes when developing software.  
<br>  

- 지극히 개인적인 기준과 실력으로 작성되었습니다. 따라서 이 모듈의 보안성, 성능 등등, 그 무엇도 보장하지 않습니다.  
It was written with extremely personal standards and skills. Therefore, we do not guarantee anything about this module's security, performance, etc.
<br>

- 모든 번역은 구글 번역기를 통해 번역되었습니다.  
All translations were translated through Google Translate.  
<br>

-----

### #2. 설치 방법.  
How to install.
<br><br>

- pip를 통해 설치가 가능하도록 만들어졌습니다. 아래 pip 명령어를 터미널 혹은 커맨드에 입력하여 바로 설치할 수 있습니다.  
It is made to be installed via pip. You can install it right away by entering the pip command below into the terminal or command.
~~~
pip install git+https://github.com/MoonsRainbow/sandbox.git
~~~  
<br><br>

#### 의존성
Dependency.
<br><br>

- 이 모듈은 pymysql (버전 1.0.2) 모듈을 사용합니다. pymysql (버전 1.0.2) 모듈은 이 모듈을 설치할 때 함께 설치됩니다.  
This module uses the pymysql (version 1.0.2) module. The pymysql (version 1.0.2) module is installed when you install this module.
<br>

- 이 모듈은 Python의 내장 모듈인 datetime을 사용합니다.  
This module uses Python's built-in module datetime.
<br>

-----

### #3. 기능 소개 - DataBaseConnManager.
Feature Introduction - DataBaseConnManager.  
<br><br>

- 이 클래스를 사용하려면 먼저 import 구문을 사용하여 불러와야 합니다.  
To use this class, you must import it using the import statement.
~~~
from sandbox import DataBaseConnManager
~~~
<br>

- 이 클래스는 데이터베이스 연결에 필요한 정보들을 입력받아 저장합니다. 입력된 정보는 데이터베이스 연결에 사용됩니다.  
This class receives and stores information needed to connect to a database. The information entered will be used to connect to the database.
~~~
example_dbcm = DatabaseConnManager({
    _host='Input your host here.',
    _port='Input your host here.',
    _user='Input your host here.',
    _pw='Input your host here.',
    _db='Input your database here. Or This argument is not required.',
})
~~~
<br>

- 입력된 정보는 mangling 처리된 인스턴스 변수로 저장되며 프로퍼티로 처리되어 있습니다.  
The entered information is stored as a mangling instance variable and processed as a property.
<br>

- 저장된 정보는 읽을 수 없으나, 다시 입력하여 설정할 수는 있습니다.  
Saved information cannot be read, but can be re-entered to set.
~~~
print(example_dbcm.host) # For security reasons, we do not provide any information.
print(example_dbcm.port) # For security reasons, we do not provide any information.
print(example_dbcm.user) # For security reasons, we do not provide any information.
print(example_dbcm.password) # For security reasons, we do not provide any information.
print(example_dbcm.database) # For security reasons, we do not provide any information.

example_dbcm.host = 'another_host'
example_dbcm.port = 'another_port'
example_dbcm.user = 'another_user'
example_dbcm.password = 'another_password'
example_dbcm.database = 'another_database'
~~~
<br>

- 아래 명령어를 사용하여 데이터베이스 연결을 생성할 수 있습니다.  
You can create a database connection using the command below.
~~~
example_dbcm.connecting()
~~~
<br>

- 아래 명령어를 사용하여 sql을 실행한 결과값을 받을 수 있습니다. 'insert' 문의 경우, 'lastrowid' 값을 반환합니다.  
You can receive the result of executing sql using the command below. For the 'insert' statement, it returns the 'lastrowid' value.
~~~
result = example_dbcm.execute_query('str type sql')
~~~
<br>

- 아래 명령어를 사용하여 데이터베이스 연결을 종료할 수 있습니다.  
You can close the database connection using the command below.
~~~
example_dbcm.disconnecting()
~~~
<br>

-----

### #4. 기능 소개 - DateManager.
Feature Introduction - DateManager.  
<br><br>

- 이 클래스를 사용하려면 먼저 import 구문을 사용하여 불러와야 합니다.  
To use this class, you must import it using the import statement.
~~~
from sandbox import DateManager
~~~
<br>

- 이 클래스는 datetime이 제공하는 datetime 형식의 데이터를 str 형식으로 변환하여 사용자에게 제공합니다.  
This class converts data in datetime format provided by datetime to str format and provides it to the user.
~~~
dt = DateManager

print(dt.current) # 2023-01-08 19:16:53.500572
print(dt.datetime) # 2023-01-08 19:16:53
print(dt.date) # 20230108
print(dt.time) # 191653
~~~
<br>

- 아래 명령어를 사용하여 날짜, 시간 형식을 설정할 수 있습니다.  
You can set the date format using the command below.
~~~
print(dt.format_datetime()) # 2023-01-08 19:19:56
print(dt.format_date()) # 2023-01-08
print(dt.format_time()) # 19:19:56

print(dt.format_datetime(d_sep='/', t_sep='`')) # 2023/01/08 19`20`46
print(dt.format_date('/')) # 2023/01/08
print(dt.format_time('`') # 19:20:46
~~~
