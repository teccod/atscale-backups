# useful commands

## clean up docker

```
docker system prune -f
```

## start container with iris

```
$ docker-compose up -d
```

## build container with no cache

```
docker-compose build --no-cache --progress=plain
```

## open terminal to docker

```
docker-compose exec iris iris session iris -U IRISAPP
```

## export IRIS Analytics artifacts

```
d ##class(dev.code).export("*.DFI")
```

## build cube

```
do ##class(%DeepSee.Utils).%BuildCube("CubeName")
```

## export globals

```
do $System.OBJ.Export("dc*.GBL","/irisdev/app/src/gbl/globals.xml",,.errors)
zw errors
```

d ##class(AtScaleBackups.utils).setConfig("NjekTt", "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", "atscale_test", "3600", "atscale.community.intersystems.com:10500", "default", "admin", "admin@is", [{ "name" : "EnCommunnityAnalytics2", "id" : "2d93c2be-5a95-4bec-6731-102eeb5c8d8d" }])
