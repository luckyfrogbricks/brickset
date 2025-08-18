#!/usr/bin/env Rscript

# load the package
library(brickset)

# configure credentials from env vars
options(
  brickset_key      = Sys.getenv("BRICKSET_KEY"),
  brickset_username = Sys.getenv("BRICKSET_USERNAME"),
  brickset_password = Sys.getenv("BRICKSET_PASSWORD")
)

# sanity‑check your key
if (!brickset::checkKey()) {
  stop("Brickset API key is not valid – double‑check your BRICKSET_KEY, USERNAME and PASSWORD")
}

# fetch all sets for 2025
sets2025 <- brickset::getSets(2025)

# write to CSV
write.csv(sets2025,
          file       = "lego_sets_2025.csv",
          row.names  = FALSE)
