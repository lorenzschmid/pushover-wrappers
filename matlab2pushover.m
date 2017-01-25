nction [response] = matlab2pushover( message )
%MATLAB2PUSHOVER Sends MESSAGE as notification via Pushover service
%   Requires internet connection and Matlab version R2015a or higher

if nargin < 1
	message = 'hello world';
end

pushoverToken = '';
userKey = '';

response = webwrite('https://api.pushover.net/1/messages', ...
    'token', pushoverToken, ...
    'user', userKey, ...
    'message', message);

end