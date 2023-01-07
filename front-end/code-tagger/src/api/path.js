let Ip = "/api/";

let path = {
  website: {
    // User
    register: Ip + "User/register",
    login: Ip + "User/login",
    exit: Ip + "User/exit",
    removeUser: Ip + "User/removeUser",
    // getUser:

    //Code
    getCodeList: Ip + "Code/getCodes",
    getCode: Ip + "Code/getCode",
    addCode: Ip + "Code/addCode",
    removeCode: Ip + "Code/removeCode",
    modifyCodeID: Ip + "Code/modifyCodeID",
    modifyCode: Ip + "Code/modifyCode",

    //Mark
    getMarkList: Ip + "Mark/getLabelMark",
    getUserMark: Ip + "Mark/getUserMark",
    addMark: Ip + "Mark/addMark",
    removeMark: Ip + "Mark/removeMark",

    //UserLabel
    getLabelList: Ip + "UserLabel/getUser",
    getLabel: Ip + "UserLabel/getLabel",
    addLabel: Ip + "UserLabel/addLabel",
    removeLabel: Ip + "UserLabel/removeLabel",
    modifyLabelID: Ip + "UserLabel/modifyLabelID",
    modifyLabelIntro: Ip + "UserLabel/modifyLabelIntro",
  },
};
export default path;
