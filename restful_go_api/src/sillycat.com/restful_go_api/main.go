package main

import "github.com/gin-gonic/gin"
import "sillycat.com/restful_go_api/waterrecord"

var DB = make(map[string]string)

func setupRouter() *gin.Engine {
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
	router := setupRouter()
	// Listen and Server in 0.0.0.0:8080
	router.Run(":8080")
}
