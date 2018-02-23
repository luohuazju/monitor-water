package main

import (
	"github.com/gin-gonic/gin"
	"github.com/spf13/viper"
	"log"
	"sillycat.com/restful_go_api/config"
	"sillycat.com/restful_go_api/waterrecord"
)

var DB = make(map[string]string)

func SetupRouter() *gin.Engine {

	// Disable Console Color
	// gin.DisableConsoleColor()
	if viper.GetBool("gin.debug") {
		log.Println("Gin is under debug mode")
	} else {
		log.Println("Gin is under prod mode")
		gin.SetMode(gin.ReleaseMode)
	}
	router := gin.Default()

	// Ping test
	router.GET("/ping", func(c *gin.Context) {
		c.String(200, "pong")
	})

	v1 := router.Group("api/v1")
	{
		v1.GET("/waterrecords", waterrecord.GetWaterRecords)
		v1.GET("/waterrecords/:id", waterrecord.GetWaterRecord)
		v1.POST("/waterrecords", waterrecord.PostWaterRecord)
		v1.PUT("/waterrecords/:id", waterrecord.UpdateWaterRecord)
		v1.DELETE("/waterrecords/:id", waterrecord.DeleteWaterRecord)
	}

	return router
}

func main() {
	config.InitViperConfig()
	router := SetupRouter()
	// Listen and Server in 0.0.0.0:8080
	port := viper.GetString("http.port")
	router.Run(":" + port)
}
