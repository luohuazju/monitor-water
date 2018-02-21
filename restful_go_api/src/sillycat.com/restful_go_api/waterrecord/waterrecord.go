package waterrecord

import (
	"github.com/gin-gonic/gin"
	"log"
	"time"
)

type WaterRecord struct {
	Id          int64
	Location    string    `xorm:"location varchar(256) not null"`
	StartTime   string    `xorm:"start_time varchar(256) not null"`
	EndTime     string    `xorm:"end_time varchar(256) not null"`
	Duration    int       `xorm:"duration int(11)"`
	ReleaseDate string    `xorm:"release_date varchar(256)"`
	CreateDate  time.Time `xorm:"create_date DATETIME "`
	UpdateDate  time.Time `xorm:"update_date DATETIME"`
}

var engine = initDatabase()

func (waterRecord WaterRecord) TableName() string {
	return "water_monitor"
}

func GetWaterRecords(c *gin.Context) {
	var items []WaterRecord
	query := "SELECT id, location, start_time, end_time, duration, release_date, create_date, update_date FROM water_monitor"
	err := engine.Sql(query).Find(&items)
	if err != nil {
		log.Fatal("Get err when exec query: ", err)
	}
	log.Println("query result: ", items)
	c.JSON(200, items)
}

func GetWaterRecord(c *gin.Context) {
	var item WaterRecord
	id := c.Param("id")

	has, err := engine.Where("id = ?", id).Get(&item)
	if err != nil {
		log.Fatal("Get one item err: ", err)
	}
	if has {
		c.JSON(200, item)
	} else {
		c.JSON(404, gin.H{"error": "WaterRecord not found"})
	}
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
