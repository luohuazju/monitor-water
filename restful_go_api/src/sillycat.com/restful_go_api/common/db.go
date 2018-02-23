package common

import (
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"github.com/go-xorm/core"
	"github.com/go-xorm/xorm"
)

func InitDatabase() *xorm.Engine {
	var engine *xorm.Engine
	var err error
	engine, err = xorm.NewEngine("mysql", "watermonitor:kaishi117A@tcp(sillycat.ddns.net:3306)/watermonitor?charset=utf8")
	if err != nil {
		fmt.Println(err)
	}
	engine.Ping()        //ping
	engine.ShowSQL(true) //show SQL
	engine.Logger().SetLevel(core.LOG_DEBUG)
	return engine
}
