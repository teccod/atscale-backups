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
    set arrProj = [
        {"name" : "mycube", "id" : "3947267f-6eee-45d5-663b-514bd71f2bb8"},
        {"name" : "mycube2", "id" : "f3a5c97f-bbae-4f09-6307-3d4e0deef91a"}
    ].%ToJSON()
    d module.setConfig(gitname, gittoken, gitrepo, delay, host, org, login, password, arrProj.%ToJSON())
}

ClassMethod setup()
{
    set module = ##class(%SYS.Python).Import("AtScaleBackupsSetup")
    w module.setup()
}

}
