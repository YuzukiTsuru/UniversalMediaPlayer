//
// Created by Ghost Gloomy on 2020/12/16.
//

#include "HTTPServer.h"

std::string HTTPServer::log() {
    std::string s;
    char buf[BUFSIZ];

    s += "================================\n";

    snprintf(buf, sizeof(buf), "%s %s %s", _req.method.c_str(), _req.version.c_str(), _req.path.c_str());
    s += buf;

    std::string query;
    for (auto it = _req.params.begin(); it != _req.params.end(); ++it) {
        const auto &x = *it;
        snprintf(buf, sizeof(buf), "%c%s=%s", (it == _req.params.begin()) ? '?' : '&', x.first.c_str(),
                 x.second.c_str());
        query += buf;
    }
    snprintf(buf, sizeof(buf), "%s\n", query.c_str());
    s += buf;

    s += dump_headers(_req.headers);

    s += "--------------------------------\n";

    snprintf(buf, sizeof(buf), "%d %s\n", _res.status, _res.version.c_str());
    s += buf;
    s += dump_headers(_res.headers);
    s += "\n";

    if (!_res.body.empty()) { s += _res.body; }
    s += "\n";
    return s;
}

std::string HTTPServer::log_bind() {
    return log();
}

std::string HTTPServer::dump_headers(const httplib::Headers &headers) {
    std::string s;
    char buf[BUFSIZ];
    for (const auto & x : headers) {
        snprintf(buf, sizeof(buf), "%s: %s\n", x.first.c_str(), x.second.c_str());
        s += buf;
    }
    return s;
}

HTTPServer::HTTPServer(const httplib::Request &req, const httplib::Response &res) {
    _req = req;
    _res = res;
}
