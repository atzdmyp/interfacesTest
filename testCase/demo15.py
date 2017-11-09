import jenkins

jenkins_server_url = "http://50.23.190.36:8080"
user_id = "chuyan"
api_token = "a13475c01866b77f9a528b9dbdc2959c"
job_name = "test"
params = {
    'params1': 'value1',
    'params2': 'value2'
}
build_number = 0
# 实例化Jenkins
server = jenkins.Jenkins(jenkins_server_url, user_id, api_token)
# 构建带参数的job
server.build_job(job_name, parameters=params)
# 获取job的相关信息
server.get_job_info(job_name)
# 获取job的最后次构建号
server.get_job_info(job_name)['lastBuild']['number']
# 获取job名为job_name的job的某次构建的执行结果状态
server.get_build_info(job_name, build_number)['result']
# 判断job名为job_name的job的某次构建是否还在构建中
server.get_build_info(job_name, build_number)['building']

