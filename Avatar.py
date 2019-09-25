from PIL import Image


class Avatar(Image.Image):
    def __init__(self, avatar_path, frame_path='AvatarFrame.png'):
        self.avatar = Image.open(avatar_path)
        self.avatar.convert('RGBA')
        self.frame = Image.open(frame_path)
        self.frame.convert('RGBA')
        self.frame_width_rate = 0.083

    def GetNewAvatar(self):
        frame_width = int(self.frame.size[0] * self.frame_width_rate)
        re_size_w, re_size_h = self.frame.size[0] - frame_width, self.frame.size[1] - frame_width
        avatar = self.avatar.resize((re_size_w, re_size_h))
        temp_avatar = Image.new('RGBA', self.frame.size)
        x1 = int(frame_width / 2)
        y1 = int(frame_width / 2)
        temp_avatar.paste(avatar, (x1, y1, x1 + re_size_w, y1 + re_size_h))
        temp_avatar.paste(self.frame, (0, 0, 2184, 2184), self.frame)
        temp_avatar.save('new_avatar.png')
