function [] = flippOut(varargin)
% flippOut.m takes a user input file an takes the central bottom region of
% the photo. The function then filters the image to enhance the thumbnail
% images found on the Flipp shirts. Following this processing a spatial
% frequency conversion is done in order to esimate the distance of the
% subject in the picture from the camera lens. This program requires an
% input of a 2560*1440. In the future this can be scalable for all image
% sizes.

imName = varargin{:};                   % Takes user input & reads it
image = im2double(imread(imName));      
image = image(1081:1440,901:1640).^0.3; % Crops the center bottom of image

% Exactly what it sounds like, a low passfilter in the x and a box filter
% in the y. This draws out the features for analysis in the x while
% blurring those in the y.
funkyfilt = [zeros(100,10) ones(100,10) zeros(100,10)];

% Padding the edges of the picture reduces edge effects. However, these
% added dimensions must be taken away later.
padImage = padarray(image,[10 10],'symmetric');
padfiltimage = (imfilter(padImage,funkyfilt));
filtimage = padfiltimage(101:270,11:750);

% This plots the process shown above. Cropped image, filtered image
% without removing padding, filtered image after padding removed.
figure(1);
subplot(3,1,1)
imshow(image,[]);
title('cropped image');
subplot(3,1,2)
imshow(padfiltimage,[]);
title('padded and filtered image');
subplot(3,1,3)
imshow(filtimage,[]);
title('filtered image');

% This loop adds all of the y values for each y coordinate.
for i = 1:length(filtimage)
    sums(i) = sum(filtimage(:,i));
end

% The fourier transform finds the frequency domain signal from the spatial
% domain image to acquire spatial frequency.          
ftSum = abs((fft(sums)));
ftSumer = ftSum(1:740);

% This plots the mean brightness spectrum and the spatial frequency of the
% image.
figure(2);
subplot(1,2,1)
plot(sums)
title('Mean Brightness')
subplot(1,2,2)
plot(ftSumer)
axis([0 50 0 4000000])
title('Spatial Frequency')

end

