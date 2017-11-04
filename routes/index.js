const express = require("express");
const router = express.Router();

router.get("/", (req, res, next) => {
  req.app.ingest.Videos.getAll({}, "", (error, { data }) => {
    return res.render("index", {
      title: "Welcome to the Ingest Starter!",
      user: req.user,
      videos: data
    });
  });
});

router.get("/video/:id", (req, res, next) => {
  req.app.ingest.Videos.getById(req.params.id, (error, { data }) => {
    const { id, title, variant_urls, description } = data;

    return res.render("player", {
      id,
      title,
      variant_urls,
      description
    });
  });
});

module.exports = router;
