package waterrecord

import (
	"github.com/gin-gonic/gin"
)

func GetWaterRecords(c *gin.Context) {
	c.JSON(200, gin.H{"ok": "GET api/v1/waterrecords"})
}

func GetWaterRecord(c *gin.Context) {
	c.JSON(200, gin.H{"ok": "GET api/v1/waterrecords/1"})
}

func PostWaterRecord(c *gin.Context) {
	c.JSON(200, gin.H{"ok": "POST api/v1/waterrecords"})

}

func UpdateWaterRecord(c *gin.Context) {
	c.JSON(200, gin.H{"ok": "PUT api/v1/waterrecords/1"})

}

func DeleteWaterRecord(c *gin.Context) {
	c.JSON(200, gin.H{"ok": "DELETE api/v1/waterrecords/1"})
}
