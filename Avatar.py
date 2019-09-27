from PIL import Image


class Avatar(Image.Image):
    def __init__(self, avatar_path):
        self.avatar = Image.open(avatar_path)
        self.avatar.convert('RGBA')
        self.frame_width_rate = 0.083

    def GetNewAvatar(self, mode='flag'):
        frame = Image.open('AvatarFrame_{}.png'.format(mode))
        frame.convert('RGBA')
        frame_width = int(frame.size[0] * self.frame_width_rate)
        re_size_w, re_size_h = frame.size[0] - frame_width, frame.size[1] - frame_width
        avatar = self.avatar.resize((re_size_w, re_size_h))
        temp_avatar = Image.new('RGBA', frame.size)
        x1 = int(frame_width / 2)
        y1 = int(frame_width / 2)
        temp_avatar.paste(avatar, (x1, y1, x1 + re_size_w, y1 + re_size_h))
        temp_avatar.paste(frame, (0, 0, 2184, 2184), frame)
        temp_avatar.save('new_avatar.png')
