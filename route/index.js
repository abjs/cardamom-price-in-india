const express = require('express')
const router = express.Router()
const User = require('../model/User.model')
  router.get("/", async(req, res) => {
    const data = await User.find({}, { _id: 0 })
    res.render("index",  {data} );
  });

  router.get("/full", async(req, res) => {
    const data = await User.find({}, { _id: 0 })
    res.render("full",  {data} );
  });

module.exports = router