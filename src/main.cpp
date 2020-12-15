#include <vlcpp/vlc.hpp>
#include <thread>
#include <iostream>

void player(const std::string& fileName){
    auto instance = VLC::Instance(0, nullptr);
    auto media = VLC::Media(instance, fileName, VLC::Media::FromPath);
    auto mp = VLC::MediaPlayer(media);
    mp.play();
    std::this_thread::sleep_for(std::chrono::seconds(10));
    mp.stop();
}

int main(int argc, char **argv) {
    player(argv[1]);
}
