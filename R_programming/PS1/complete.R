complete <- function(directory, id = 1:332) {
    readPollutant <- function(directory, id) {
        read.csv(paste(directory, "/", sprintf("%03d", id), ".csv", sep=''))
    }
    
    nobs = numeric(0)
    
    for(i in id) {
        csv <- readPollutant(directory, i)
        nobs = c(nobs, sum(!is.na(csv$sulfate) & !is.na(csv$nitrate)))
    }
    
    data.frame(id=id, nobs=nobs)
}

complete("specdata", 1)