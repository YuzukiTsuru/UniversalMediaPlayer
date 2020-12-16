//
// Created by Ghost Gloomy on 2020/12/16.
//

#ifndef UNIVERSALMEDIAPLAYER_HTTPSERVER_H
#define UNIVERSALMEDIAPLAYER_HTTPSERVER_H
#include <iostream>
#include <httplib.h>

class HTTPServer {
public:
    HTTPServer(const httplib::Request &req, const httplib::Response &res);

    std::string log_bind();

private:
    std::string log();
    static std::string dump_headers(const httplib::Headers &headers);

    httplib::Request _req;
    httplib::Response _res;
};


#endif //UNIVERSALMEDIAPLAYER_HTTPSERVER_H
