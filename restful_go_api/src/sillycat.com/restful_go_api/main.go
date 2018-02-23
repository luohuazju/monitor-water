package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"github.com/spf13/viper"
	"log"
	"os"
	"sillycat.com/restful_go_api/waterrecord"
)

var DB = make(map[string]string)

const appName = "config"

func SetupRouter() *gin.Engine {

	// Disable Console Color
	// gin.DisableConsoleColor()
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
	log.Println("Start to init the config--------")
	viper.SetDefault("http.port", "8080")

	if os.Getenv("ENVIRONMENT") == "DEV" {
		log.Println("system is running under DEV mode")
		viper.SetConfigName(appName + "-dev") // name of config file (without extension)
	} else {
		log.Println("system is running under PROD mode")
		viper.SetConfigName(appName + "-prod") // name of config file (without extension)
	}
	viper.AddConfigPath("/etc/" + appName + "/") // path to look for the config file in
	viper.AddConfigPath("./")                    // optionally look for config in the working directory
	viper.AddConfigPath("./conf/")
	viper.AutomaticEnv()
	err := viper.ReadInConfig() // Find and read the config file
	if err != nil {             // Handle errors reading the config file
		panic(fmt.Errorf("Fatal error config file: %s \n", err))
	}

	router := SetupRouter()
	// Listen and Server in 0.0.0.0:8080
	port := viper.GetString("http.port")
	router.Run(":" + port)
}
