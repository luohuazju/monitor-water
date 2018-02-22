#restful_go_api

Prepare the library

>go get github.com/gin-gonic/gin

>go get github.com/go-xorm/xorm

>go get github.com/go-sql-driver/mysql

How to Build for local

>go install sillycat.com/restful_go_api

How to Run Test

>go test sillycat.com/restful_go_api

How to Build for Linux

>env GOOS=linux GOARCH=amd64 go build -o bin/restful_go_api_linux -v sillycat.com/restful_go_api

How to Build for Raspberrypi

>env GOOS=linux GOARCH=arm GOARM=7 go build -o bin/restful_go_api_arm -v sillycat.com/restful_go_api

How to Run

>bin/restful_go_api

For developer

Install golang dep on your system

>dep ensure