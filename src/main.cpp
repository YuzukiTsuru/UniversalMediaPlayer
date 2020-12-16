#include <vlcpp/vlc.hpp>
#include <httplib.h>
#include <thread>
#include <iostream>

#include "HTTPServer.h"

void player(const std::string &fileName) {
    auto instance = VLC::Instance(0, nullptr);
    auto media = VLC::Media(instance, fileName, VLC::Media::FromPath);
    auto mp = VLC::MediaPlayer(media);
    mp.play();
    std::this_thread::sleep_for(std::chrono::seconds(10));
    mp.stop();
}

int main(int argc, char **argv) {
    httplib::Server svr;
    svr.Post("/", [](const httplib::Request &req, httplib::Response &res) {
        auto play = req.get_param_value("PlayID");
        player(play);
    });

    svr.set_logger([](const httplib::Request &req, const httplib::Response &res){
        HTTPServer httpServer(req, res);
        std::cout << httpServer.log_bind() << std::endl;
    });
    svr.listen("0.0.0.0", 8080);
}
