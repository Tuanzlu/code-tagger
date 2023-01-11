let Ip = "/api/";

let path = {
  website: {
    // User
    register: Ip + "User/register",
    login: Ip + "User/login",
    exit: Ip + "User/exit",
    modifyPW: Ip + "User/modifyPassword",
    removeUser: Ip + "User/removeUser",
    // Admin:
    getUserList: Ip + "Admin/getUsers",
    admin_removeUser: Ip + "Admin/removeUser",

    //Code
    getCodeList: Ip + "Code/getCodes",
    getCode: Ip + "Code/getCode",
    addCode: Ip + "Code/addCode",
    removeCode: Ip + "Code/removeCode",
    modifyCodeID: Ip + "Code/modifyCodeID",
    modifyCode: Ip + "Code/modifyCode",

    //Mark
    getLabelMark: Ip + "Mark/getLabelMark",
    getUserMark: Ip + "Mark/getUserMark",
    addMark: Ip + "Mark/addMark",
    removeMark: Ip + "Mark/removeMark",
    getCodeMark: Ip + "Mark/getCodeMark",

    //UserLabel
    getLabelList: Ip + "UserLabel/getUser",
    getLabel: Ip + "UserLabel/getLabel",
    addLabel: Ip + "UserLabel/addLabel",
    removeLabel: Ip + "UserLabel/removeLabel",
    modifyLabelID: Ip + "UserLabel/modifyLabelID",
    modifyLabelIntro: Ip + "UserLabel/modifyLabelintro",
  },
};
export default path;
