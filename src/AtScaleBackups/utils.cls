Class AtScaleBackups.utils
{

ClassMethod start()
{
    set module = ##class(%SYS.Python).Import("AtScaleBackups")
    w module.start()
}

ClassMethod setConfig(gitname, gittoken, gitrepo, delay, host, org, login, password, projects)
{
    set module = ##class(%SYS.Python).Import("AtScaleBackups")
    d module.setConfig(gitname, gittoken, gitrepo, delay, host, org, login, password, projects.%ToJSON())
}

ClassMethod setup()
{
    set module = ##class(%SYS.Python).Import("AtScaleBackupsSetup")
    w module.setup()
}

}
