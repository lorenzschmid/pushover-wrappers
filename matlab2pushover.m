function [] = matlab2pushover(message)
if nargin<1
	message='hello world';
end
pushoverToken='';
userKey='';
system(['curl -s -F "token=',pushoverToken,'" -F "user=',userKey,'" -F "message=',message,'" https://api.pushover.net/1/messages'])
end