package common

import (
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"github.com/go-xorm/core"
	"github.com/go-xorm/xorm"
	"github.com/spf13/viper"
	"sillycat.com/restful_go_api/config"
)

var engine = InitDatabase()

func InitDatabase() *xorm.Engine {

	config.InitViperConfig()

	var engine *xorm.Engine
	var err error

	dbType := viper.GetString("database.type")

	engine, err = xorm.NewEngine(dbType, "watermonitor:kaishi117A@tcp(sillycat.ddns.net:3306)/watermonitor?charset=utf8")
	if err != nil {
		fmt.Println(err)
	}
	engine.Ping()        //ping
	engine.ShowSQL(true) //show SQL
	engine.Logger().SetLevel(core.LOG_DEBUG)
	return engine
}

func GetDatabase() *xorm.Engine {
	return engine
}
